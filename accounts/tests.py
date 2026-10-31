from django.test import TestCase
from django.urls import reverse


class RegistrationViewTests(TestCase):
    def test_registration_page_renders_form(self):
        response = self.client.get(reverse("accounts:register"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")
        self.assertIn("form", response.context)

    def test_invalid_registration_preserves_form_errors(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newuser",
                "password1": "StrongPassword123!",
                "password2": "DifferentPassword123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(response.context["form"]["username"].value(), "newuser")
