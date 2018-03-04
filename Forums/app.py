import dummy_data
import memberstore
from flask import Flask, render_template

app = Flask(__name__)

member_store = memberstore.MemberStore()
post_store = memberstore.PostStore()

from views import *

if __name__  == "__main__":
    dummy_data.seed_stores(member_store, post_store)
    app.run()
app.run()