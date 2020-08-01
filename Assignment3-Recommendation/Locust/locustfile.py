from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def hello_world(self):
        self.client.get("http://127.0.0.1:8000/SARpredict?userID=1")
        
    @task(1)
    def hello_world(self):
        self.client.get("http://127.0.0.1:8000/RBMpredict?userID=1")
