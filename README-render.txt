
CCTV Site - Ready for deployment on Render (or similar services)
===============================================================

This repository contains a Flask web app that serves the "أنماط المراقبة الأمنية" site.
It includes an admin panel to edit products, services and contact phone (password: 1234).
The app stores data in local JSON files (data/*.json).

Files of interest:
- flask_app.py        -> Flask application
- requirements.txt    -> Python dependencies (Flask + Gunicorn)
- Procfile            -> Command for Render to start the app
- runtime.txt         -> Python runtime
- data/               -> products.json, services.json, contact.json (initial data)
- templates/ and static/ -> site HTML/CSS/images
- README-render.txt   -> deployment notes for Render

Quick Deploy to Render.com (recommended):
1) Create a GitHub repository and push the contents of this folder to it.
   Example (local machine):
     git init
     git add .
     git commit -m "Initial deploy"
     git branch -M main
     git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
     git push -u origin main

2) Sign in to Render (https://render.com) and click "New" -> "Web Service".
3) Connect your GitHub and choose the repository you just pushed.
4) For "Build Command" put: pip install -r requirements.txt
   For "Start Command" put: gunicorn flask_app:app --bind 0.0.0.0:$PORT
5) Click "Create Web Service" and Render will build and deploy. After a few minutes you'll get a public URL.
6) Open URL + /admin to access the admin panel (password: 1234).

Notes:
- The app writes JSON files to disk. On Render, the filesystem is ephemeral between deploys; for persistent data either:
  a) Use Render's managed PostgreSQL and update the app to save data there, or
  b) Store backups/exported JSON to an external store (S3) or commit changes to Git (advanced).
- For quick testing and demonstration this repo works as-is on Render's free tier.

If you want, I can:
- Prepare a GitHub repo zip ready to upload (this file), and give you exact one-click Render steps.
- Or, if you prefer, I can attempt to deploy it to my own Render account and give you a demo link (temporary).

