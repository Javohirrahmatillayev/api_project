from rest_framework.permissions import BasePermission
from django.utils import timezone
from datetime import timedelta

class CanUpdateWithin4Hours(BasePermission):
    message = "You can edit this object within 4 hours"
    
    def has_object_permission(self, request, view, obj):
        if request.method not in ['PUT', 'PATCH']:
            return True
        
        time_limit = obj.created_at + timedelta(hours=4)
        return timezone.now() <= time_limit