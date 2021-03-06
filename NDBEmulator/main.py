import mock
from flask import Flask
from google.cloud import ndb
from google.cloud.ndb import metadata

import google.auth.credentials
import os

#webapp3 is optional if you'd rather just use Flask in a traditional manner
from webapp3 import *

os.environ["DATASTORE_DATASET"] = "test"
os.environ["DATASTORE_EMULATOR_HOST"] = "127.0.0.1:8001"
os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "127.0.0.1:8001/datastore"
os.environ["DATASTORE_HOST"] = "http://127.0.0.1:8001"
os.environ["DATASTORE_PROJECT_ID"] = "test"

app = Flask(__name__)

credentials = mock.Mock(spec=google.auth.credentials.Credentials)
db = ndb.Client(project="test", credentials=credentials)

htmlHome="""
<!DOCTYPE html>
<html>
    <head></head>
    <body>
        It has been logged that you went to the home page
    </body>
</html>
"""

html1="""
<!DOCTYPE html>
<html>
    <head></head>
    <body>
"""
html2="""
 </body>
</html>
"""

class Basic(ndb.Model):
  name = ndb.StringProperty()

@app.route("/")
def index():
    # add object to db
    client = ndb.Client(project="test", credentials=credentials)
    with client.context():
        entity = Basic()
        entity.name= "went to the home page"
        entity.put()

        return htmlHome


class Test(BaseHandler):
    def get(self):
        client = ndb.Client(project="test", credentials=credentials)
        with client.context():
            self.response.write(html1)
            basicSearch=ndb.gql("select * from Basic")
            for a in basicSearch:
                self.response.write(a.name)
            self.response.write(html2)

            
class NDBViewer(BaseHandler):
    def get(self):
        client = ndb.Client(project="test", credentials=credentials)
        with client.context():

            self.response.write(html1)
            daKinds=metadata.get_kinds()
            self.response.write("""
            Please choose the kind that you would like to view
            <form method="post" action="/NDBViewer">
                <select name="Kind">
            """)
            for a in daKinds:
                self.response.write("<option value='{a}'>{a}</option>".format(a=str(a)))
            self.response.write("""
            </select>
            <input type="submit">
            </form>
            """)
            self.response.write(html2)
    def post(self):
        client = ndb.Client(project="test", credentials=credentials)
        with client.context():

            self.response.write(html1)
            daKinds=metadata.get_kinds()
            self.response.write("""
            <style>
            table, th, td {
  border: 1px solid black;
}
            </style>
            Please choose the kind that you would like to view
            <form method="post" action="/NDBViewer">
                <select name="Kind">
            """)
            for a in daKinds:
                self.response.write("<option value='{a}'>{a}</option>".format(a=a))
            self.response.write("""
            <input type="submit">
            </select>
            </form>
            """)
            disKind=self.request.get("Kind")
            daprops=metadata.get_properties_of_kind(disKind)
            self.response.write("""
            <table><tr>
            """)
            for c in daprops:
                self.response.write("<th>"+c+"</th>")
            self.response.write("""
            </tr>
            """)
            BasicSearch=ndb.gql("Select * from {disKind} limit 50".format(disKind=disKind))
            for b in BasicSearch:
                self.response.write("""
                 <tr>
                """)
                for c in daprops:
                    davar=getattr(b,c)
                    self.response.write("<td>"+davar+"</td>")
                self.response.write("""
                 </tr>
                """)
            self.response.write("</table>")

            self.response.write(html2)            
            
@app.route('/<searchURL>',methods=['GET','POST'])    
def RouteDef(searchURL):    
    app = webapp2.WSGIApplication([
    ("/test", Test),
    ("/NDBViewer", NDBViewer),
    ]
    , searchURL=searchURL ) #when you paste in your old webapp2 handler make sure to remove 
    return webapp(app()) 


if __name__ == '__main__':
    app.run(port=5000, host="127.0.0.1")
