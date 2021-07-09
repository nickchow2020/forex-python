from unittest import TestCase
from forex_python.converter import RatesNotAvailableError
from app import app

app.config["DEBUG_TB_HOSTS"]=["dont-show-debug-toolbar"]
app.config["TESTING"] = True

class Flask_integration(TestCase):
    def test_home_get(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

        self.assertEqual(res.status_code,200)
        self.assertIn("<title>Currency Converter</title>",html)
    
    def test_home_post(self):
        with app.test_client() as client:
            res = client.post("/",data={"from":"USD","to":"CNY","amount":"1"},follow_redirects=True)
            html = res.get_data(as_text=True)
        self.assertEqual(res.status_code,200)
        self.assertIn("<p>The result is ¥6.49</p>",html)

    def test_home_post_err1(self):
        with app.test_client() as client:
            res = client.post("/",data={"from":"aasda","to":"CNY","amount":"1"},follow_redirects=True)
            html = res.get_data(as_text=True)
        self.assertEqual(res.status_code,200)
        self.assertIn('<li class="message">Please entry a valid currency value: aasda</li>',html)

    def test_home_post_err2(self):
        with app.test_client() as client:
            res = client.post("/",data={"from":"USD","to":"CNY","amount":"hello"},follow_redirects=True)
            html = res.get_data(as_text=True)
        self.assertEqual(res.status_code,200)
        self.assertIn('<li class="message">Please entry a valid amount value: hello</li>',html)

    def test_result(self):
        with app.test_client() as client:
            res = client.get("/result?currency-rate=1234&currency-symbal=$")
            html = res.get_data(as_text=True)

        self.assertEqual(res.status_code,200)
        self.assertIn("<p>The result is $1234</p>",html)
