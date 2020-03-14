import app, unittest

from app import array 

class SocketIOTestCase(unittest.TestCase):
    pass
    def test_server_sends_hello(self):
        client = app.socketio.test_client(app.app)
        response = client.get_received()
        self.assertEquals(len(response), 1)
        from_server = response[0]
        
        self.assertEqual(
            from_server['data'], 
            "message array"
        )
        data = from_server["args"][0]
        self.assertEqual(data['message'], array)

if __name__ == "__main__":
    unittest.main()
