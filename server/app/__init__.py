#!/usr/bin/python3
"""
__init__ file for importing app views
"""

from flask import Blueprint

app = Blueprint("app", __name__, url_prefix="/api/v1")

from app.repo_stars import *
