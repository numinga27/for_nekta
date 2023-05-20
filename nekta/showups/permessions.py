from rest_framework import permissions

class IsRequestAuthorOrAdmin(permissions.BasePermission):
    '''Пермишен для тех кто имеет права видеть и создавать заявки и сообщения'''
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        elif view.action == 'list' or view.action == 'retrieve':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff