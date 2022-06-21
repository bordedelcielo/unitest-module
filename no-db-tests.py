from unittest import TestCase, main
from match import match
from main import app
import json

class MatchTestCase(TestCase):
    
    def test_1_empty_match(self):
        self.assertTrue(match('',''))

    def test_2_all_plus(self):
        self.assertTrue(match('++++++++++++++','testinput'))

    def test_3_all_plus_start(self):
        self.assertTrue(match('t++++++++++++++','testinput'))

    def test_4_all_plus_end(self):
        self.assertTrue(match('++++++++++++++t','testinput'))

class AppTestCase(TestCase):
    def setUp(self):
        self.client=app.test_client(self)
    
    def test_1_index_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_2_index_ct(self):
        response = self.client.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_3_index_data(self):
        response = self.client.get('/')
        self.assertTrue(b'Guys' in response.data)

    def test_4_word_(self):
        response=self.client.get('/word')
        self.assertEqual(response.status_code, 200)

    def test_5_word_content(self):
        response=self.client.get('/word')
        self.assertEqual(response.content_type, 'application/json')

    def test_6_word_data(self):
        response=self.client.get('/word')
        self.assertTrue(b'[]' in response.data)

    def test_7_word_post_list_response(self):
        response=self.client.post('/word', data=json.dumps(['another','word']))
        self.assertTrue(response.status_code, 201)

    def test_7_word_post_list_ct(self):
        response=self.client.post('/word', data=json.dumps(['another','word'])) 
        self.assertTrue(response.content_type, 'application/json')  


    def test_7_word_post_list_data(self):
        response=self.client.post('/word', data=json.dumps(['another','word']))
        self.assertTrue((b'another' in response.data and b'word' in response.data))




if __name__ == "__main__":
    main()