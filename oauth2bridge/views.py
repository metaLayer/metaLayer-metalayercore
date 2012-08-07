from django.http import HttpResponse
from metalayercore.oauth2bridge.controllers import GoogleOauth2Controller

def handle_google_oauth2_callback(request):
    GoogleOauth2Controller.HandleOauth2Return(request)
    return HttpResponse("""
        <html>
            <head>
                <script type='text/javascript' language='javascript'>
                    window.close()
                </script>
            </head>
        </html>
    """)