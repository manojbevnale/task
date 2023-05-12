from rest_framework.throttling import SimpleRateThrottle

class UserListThrottle(SimpleRateThrottle):
    rate = '5/minute'

    def get_cache_key(self, request, view):
        return self.get_ident(request)
