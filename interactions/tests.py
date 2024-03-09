from django.test import TestCase
from django.urls import reverse
from interactions.models import Message

class InteractionsTestCase(TestCase):
    def test_send_message(self):
        # Create a test message
        message_text = "Hello, this is a test message."
        sender_id = 1  # Replace with the ID of the sender
        receiver_id = 2  # Replace with the ID of the receiver
        message = Message.objects.create(sender_id=sender_id, receiver_id=receiver_id, content=message_text)

        # Retrieve the message from the database
        retrieved_message = Message.objects.get(pk=message.id)

        # Check if the message was created successfully
        self.assertEqual(retrieved_message.content, message_text)
        self.assertEqual(retrieved_message.sender_id, sender_id)
        self.assertEqual(retrieved_message.receiver_id, receiver_id)

    def test_message_view(self):
        # Create a test message
        message_text = "Hello, this is a test message."
        sender_id = 1  # Replace with the ID of the sender
        receiver_id = 2  # Replace with the ID of the receiver
        message = Message.objects.create(sender_id=sender_id, receiver_id=receiver_id, content=message_text)

        # Access the view to retrieve the message
        response = self.client.get(reverse('message_detail', kwargs={'pk': message.id}))

        # Check if the view returns the correct message
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, message_text)
        self.assertContains(response, sender_id)
        self.assertContains(response, receiver_id)
