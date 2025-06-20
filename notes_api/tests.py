from django.test import TestCase

from rest_framework.test import APIClient

from rest_framework import status

from .models import Notes


class NotesAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.note = Notes.objects.create(title="Test Title", content="Test content")

    def test_get_all_notes(self):
        # Simple get request - similar to requests library, 200 signals it worked
        response = self.client.get("/api/notes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_note(self):
        # Added refresh from db because it was having issues for some strange reason
        # a print statement initially fixed it.
        # This also fixed and seemed cleaner.
        self.note.refresh_from_db()
        response = self.client.get(f"/api/notes/{self.note.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Title")

    def test_create_note(self):
        # Create new note, with amazing content section, 10/10
        data = {"title": "Note", "content": "Blah blah"}
        response = self.client.post("/api/notes/", data)
        # post responds with 201 ofc
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notes.objects.count(), 2)

    def test_update_note(self):
        # Updated, even better of a content, 12/10 do recommend
        data = {"title": "Note Update", "content": "Updated Blah blah!"}
        response = self.client.put(f"/api/notes/{self.note.id}/", data)
        # put sends a 200 request the same as GET, did not know this till now. The more you know
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Refresh because same as above, running a bit too fast for the db? not sure.
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Note Update")

    def test_delete_note(self):
        # Simple delete. 0 Objects remaining.
        response = self.client.delete(f"/api/notes/{self.note.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Notes.objects.count(), 0)
