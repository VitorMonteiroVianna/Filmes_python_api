from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')
        if request.mothod == 'POST':
            return request.user.has_perm('genres.post_genre')
        
        return False