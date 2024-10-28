import uuid
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import EmailStatus
from .serializers import EmailStatusSerializer
from django.conf import settings
import requests


class SendBulkEmailView(APIView):
    def post(self, request):
        emails = request.data.get("emails")
        if not emails:
            return Response(
                {"error": "No emails provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        for email in emails.split(","):
            tracking_hash = uuid.uuid4().hex
            tracking_url = (
                f"{request.build_absolute_uri('/tracker/track/')}?hash={tracking_hash}"
            )

            message = (
                '''\
                <html>
                <body>
                    <p>Hi,<br>
                    A 1x1 pixel is here somewhere try and find it! ;)</p>
                    <img src="'''
                + tracking_url
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
    def get(self, request):
        tracking_hash = request.GET.get("hash")
        if tracking_hash:
            email_status = get_object_or_404(EmailStatus, tracking_hash=tracking_hash)
            email_status.status = "opened"
            email_status.save()
            # Fetch the actual image and return it
            image_url = (
                "https://cdn.pixabay.com/photo/2022/01/11/21/48/link-6931554_640.png"
            )
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                return HttpResponse(image_response.content, content_type="image/png")
            else:
                return HttpResponse(status=404)

        # If no hash or image is not found, raise a 404
        return HttpResponse(status=404)
