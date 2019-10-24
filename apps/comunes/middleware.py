from apps.comunes import utils

class CurrentUserMiddleware:
    def process_request(self, request):
        utils.set_current_user(getattr(request, 'user', None))



class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        utils.set_current_user(getattr(request, 'user', None))
        response = self.get_response(request)
        utils.remove_current_user()
        return response
