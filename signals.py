@receiver(post_save, sender=BaseAddress.__subclasses__())
@receiver(post_save, sender=StudentAddress)
def student_zoneing(sender, instance, **kwargs):
    if instance.pk is not None:
        logger.info("Re-zoned after address is changed: %s", instance)
        instance.re_zoning()
        
        
        
 # models.py
    def re_zoning(self):
        """update hs ms and es zones for student address upon the address is changed
        """
        try: 
            from core.tasks import get_zoned_address
            zone_dict = get_zoned_address(self.street_number, self.street_name, self.zip_code)
            kwargs = dict()
            _zone_dict = copy.deepcopy(zone_dict)  # This one needs to be serializable.
            if zone_dict.get('zoned_es_school'):
                kwargs['zoned_es_school'] = zone_dict['zoned_es_school']
                _zone_dict['zoned_es_school'] = str(_zone_dict['zoned_es_school'])
            if zone_dict.get('zoned_ms_school'):
                kwargs['zoned_ms_school'] = zone_dict['zoned_ms_school']
                _zone_dict['zoned_ms_school'] = str(_zone_dict['zoned_ms_school'])
            if zone_dict.get('zoned_hs_school'):
                kwargs['zoned_hs_school'] = zone_dict['zoned_hs_school']
                _zone_dict['zoned_hs_school'] = str(_zone_dict['zoned_hs_school'])
            if zone_dict.get('district_code'):
                kwargs['district'] = District.objects.filter(code=zone_dict['district_code']).first()
                if kwargs['district']:
                    kwargs['borough'] = kwargs['district'].borough
            kwargs['zone_response'] = _zone_dict
            address_id = self.id
            # NO: Do it this way so that save() and signals don't run again.
            StudentAddress.objects.filter(id=address_id).update(**kwargs)
            return (self.pk, _zone_dict)
        except Exception as e: # pylint: disable=broad-except 
            print('Error updating zoned schools for: {}, {}'.format(e, self))
