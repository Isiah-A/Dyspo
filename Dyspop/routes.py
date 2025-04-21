from flask import render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required
import datetime
import markdown
from flask import Blueprint, render_template, request, redirect, url_for

rt = Blueprint('routes', __name__)



