from rest_framework import permissions


class EhSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:  # verifica se é superuser pra poder deletar
                return True
            return False
        return True
