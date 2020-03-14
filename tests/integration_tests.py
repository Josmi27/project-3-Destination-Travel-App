import app, unittest, requests, flask_testing

class ServerIntegrationTestCase(
    flask_testing.LiveServerTestCase
):
        
    def create_app(self):
        return app.app

    def test_server_running(self):
        response = requests.get(self.get_server_url())
        self.assertEqual(response.status_code, 200)
        print(response)
     
    

if __name__ == '__main__':
    unittest.main()