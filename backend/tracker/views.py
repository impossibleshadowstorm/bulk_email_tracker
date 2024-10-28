import uuid
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import EmailStatus
from django.conf import settings
import os
from django.views.static import serve


class SendBulkEmailView(APIView):
    def post(self, request):
        emails = request.data.get("emails")
        if not emails:
            return Response(
                {"error": "No emails provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        for email in emails.split(","):
            tracking_hash = uuid.uuid4().hex
            tracking_url = f"{request.build_absolute_uri(f'/api/tracker/track/{tracking_hash}/abc.jpg')}"

            message = (
                '''\
                <html>
                <body>
                    <p>Hi,<br>
                    A 1x1 pixel is here somewhere try and find it! ;)</p>
                    <img src="'''
                + tracking_url.replace("http://", "https://")
                + """">
                </body>
                </html>
            """
            )

            # Send email with tracking image
            # message = f"""
            #     <html>
            #         <body>
            #             <p>Dear User,</p>
            #             <p>This is a test email. Please open this email to confirm.</p>
            #             <!-- Tracking image -->
            #             <img src="{tracking_url}" alt="Tracking Image" width="1" height="1" style="display:none;"/>
            #             <p>Regards,</p>
            #             <p>Your Company</p>
            #         </body>
            #     </html>
            # """
            try:
                send_mail(
                    subject="Tracking Email",
                    message="Please view this email in HTML format.",
                    html_message=message,
                    recipient_list=[email],
                    from_email=settings.DEFAULT_FROM_EMAIL,
                )

                # Create EmailStatus entry
                EmailStatus.objects.create(
                    email=email.strip(), tracking_hash=tracking_hash
                )
            except Exception as e:
                # Track failures if email sending fails
                EmailStatus.objects.create(
                    email=email.strip(), tracking_hash=tracking_hash, status="failed"
                )

        return Response(
            {"message": "Emails sent successfully"}, status=status.HTTP_200_OK
        )


class TrackEmailOpenView(APIView):
    def get(self, request, hash):
        # Get the email status based on the tracking hash
        email_status = get_object_or_404(EmailStatus, tracking_hash=hash)
        email_status.status = "opened"
        email_status.save()

        # Path to your local tracking image
        image_path = os.path.join(settings.BASE_DIR, "static", "images", "abc.jpg")

        # Ensure the image exists
        if os.path.exists(image_path):
            with open(image_path, "rb") as image_file:
                # Set the appropriate content type
                response = HttpResponse(image_file.read(), content_type="image/jpeg")
                response["Content-Disposition"] = (
                    'inline; filename="abc.jpg"'  # Optional: For direct download
                )
                return response

        # If the image is not found, return a 404 status
        return HttpResponse(status=404)
