from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item, List

# Create your tests here.

#
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):

        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Create a HttpRequest object
        request = HttpRequest()
        # transfer the object to the home_page view.
        response = home_page(request)

        # The reason using b'' is because in the response.content, the content is in origin code
        # not in python code.

        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))

        # We can use render_to_string to test our templates
        expected_html = render_to_string('home.html')
        # decode translate the Python language to Unicode
        self.assertEqual(response.content.decode(), expected_html)

    # def test_home_page_can_save_a_POST_request(self):
    #
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = home_page(request)
    #
    #     self.assertEqual(Item.objects.count(), 1)
    #     # Item.objects.count() = Item.objects.all().count()
    #     new_item = Item.objects.first()
    #     # Item.objects.first() = Item.objects.all()[0]
    #     self.assertEqual(new_item.text, 'A new list item')

    # def test_home_page_redirects_after_POST(self):
    #
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = home_page(request)
    #
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    # def test_home_page_only_saves_items_when_necessary(self):
    #     request = HttpRequest()
    #     home_page(request)
    #     self.assertEqual(Item.objects.count(), 0)

    # def test_home_page_displays_all_list_items(self):
    #     Item.objects.create(text='itemey 1')
    #     Item.objects.create(text='itemey 2')
    #
    #     request = HttpRequest()
    #     response = home_page(request)
    #
    #     self.assertIn('itemey 1', response.content.decode())
    #     self.assertIn('itemey 2', response.content.decode())


#class ItemModelTest(TestCase):
class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_list_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)

        # client is an attribute of the TestCase, use GET to visit target URL
        response = self.client.get('/lists/the-only-list-in-the-world/')

        # This attribute, provided by Django can tell how to process response and
        # react to its contained strings
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):

    def test_saving_a_POST_request(self):

        # get have a '/' at the end while post doesn't have such /
        self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'},
        )

        self.assertEqual(Item.objects.count(), 1)
        # Item.objects.count() = Item.objects.all().count()
        new_item = Item.objects.first()
        # Item.objects.first() = Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):

        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'},
        )

        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
