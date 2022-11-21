  from django.core.cache import cache
  
  cache_key_guardian = 'uasi_guardian_%s' % instance.pk)
    update_addr_student_ids = Students.objects.filter(grade=5).values_list('id', flat=True)
    cache.set(cache_key_guardian, update_addr_student_ids)

    update_addr_student_ids = cache.get(cache_key_guardian, list())
