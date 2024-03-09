from django.test import TestCase
from django.urls import reverse
from session.models import ClassType, YogaClass

class SessionTestCase(TestCase):
    def setUp(self):
        # Create test class types
        self.yoga_type1 = ClassType.objects.create(name="Hatha Yoga")
        self.yoga_type2 = ClassType.objects.create(name="Vinyasa Yoga")

        # Create test yoga classes
        self.yoga_class1 = YogaClass.objects.create(
            title="Morning Hatha Yoga",
            class_type=self.yoga_type1,
            date="2024-02-21",
            time="08:00",
            location="Yoga Studio A",
            classroom_equipment="Yoga mats, blocks, straps",
            description="A gentle morning hatha yoga class for all levels."
        )
        self.yoga_class2 = YogaClass.objects.create(
            title="Evening Vinyasa Flow",
            class_type=self.yoga_type2,
            date="2024-02-22",
            time="18:00",
            location="Yoga Studio B",
            classroom_equipment="Yoga mats, blankets",
            description="An invigorating vinyasa flow class to unwind after work."
        )

    def test_yoga_class_list_view(self):
        # Access the yoga class list view
        response = self.client.get(reverse('yoga_class_list'))

        # Check if the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check if both yoga classes are present in the response context
        self.assertIn(self.yoga_class1, response.context['yoga_classes'])
        self.assertIn(self.yoga_class2, response.context['yoga_classes'])

    def test_class_detail_view(self):
        # Access the detail view of a specific yoga class
        response = self.client.get(reverse('class_detail', args=[self.yoga_class1.id]))

        # Check if the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check if the details of the yoga class are present in the response
        self.assertContains(response, self.yoga_class1.title)
        self.assertContains(response, self.yoga_class1.tutor)
        self.assertContains(response, self.yoga_class1.description)
