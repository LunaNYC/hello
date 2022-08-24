class MyAdmin(...):    
  # first_name short_description won't work in the list, we have to use a new method to show it
  list_display = ('get_first_name',)    
  readonly_fields = ('get_first_name', )        
  def get_first_name(self, obj):
        """ When use this in the admin page, 
        """
        icons = ''
        if obj.bio_biogdata_status == Student.STATUS_DISCHARGED:
            icons += ' <span style="color:red" title="Discharged">-</span> '
        elif obj.when_created and obj.when_created >= timezone.now() - datetime.timedelta(days=14):
            icons += ' <span style="color:green" title="New Student">+</span> '
        return mark_safe('%s%s' % (icons, obj.first_name))
    get_first_name.short_description = 'First Name'
