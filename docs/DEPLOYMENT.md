# Deploying to Streamlit Cloud

This guide will help you deploy your AI Text Summarizer to Streamlit Cloud.

## Prerequisites

1. A [GitHub](https://github.com) account
2. A [Streamlit Cloud](https://streamlit.io/cloud) account (sign up with GitHub)
3. An [OpenRouter](https://openrouter.ai/) API key

## Step 1: Push Your Code to GitHub

1. Create a new repository on GitHub
2. Push your code to the repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

**Important:** The `.gitignore` file already excludes `.streamlit/secrets.toml`, so your local API key won't be committed.

## Step 2: Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click **"New app"**
3. Select your repository, branch, and main file:
   - **Repository:** `YOUR_USERNAME/YOUR_REPO`
   - **Branch:** `main`
   - **Main file path:** `app.py`

## Step 3: Configure Secrets

1. Before deploying, click on **"Advanced settings"**
2. In the **Secrets** section, add your OpenRouter API key:

```toml
OPENROUTER_KEY = "sk-or-v1-your-actual-api-key-here"
```

3. Click **"Save"**

## Step 4: Deploy

1. Click **"Deploy"**
2. Wait for the app to build and deploy (usually takes 1-2 minutes)
3. Your app will be available at a URL like: `https://your-app-name.streamlit.app`

## Updating Your App

After deployment, any changes you push to your GitHub repository will automatically trigger a redeployment:

```bash
git add .
git commit -m "Description of changes"
git push
```

## Managing Secrets After Deployment

To update your API key or other secrets after deployment:

1. Go to your app on Streamlit Cloud
2. Click the menu (⋮) in the top right
3. Select **"Settings"**
4. Navigate to **"Secrets"**
5. Update the secrets in TOML format
6. Click **"Save"**
7. The app will automatically reboot with the new secrets

## Troubleshooting

### App Won't Start

**Error:** "Missing OPENROUTER_KEY in secrets"
- **Solution:** Check that you've added the secret in the correct TOML format in your app settings

### API Errors

**Error:** "Error making API request: 401 Unauthorized"
- **Solution:** Your API key may be invalid. Update it in the Secrets section

### Build Fails

**Error:** "Could not find requirements.txt"
- **Solution:** Ensure `requirements.txt` is in the root of your repository and committed to GitHub

## Best Practices

1. **Keep secrets secret:** Never commit API keys to your repository
2. **Monitor usage:** Check your OpenRouter dashboard for API usage and rate limits
3. **Version control:** Use meaningful commit messages for tracking changes
4. **Test locally:** Always test changes locally before pushing to production
5. **Resource limits:** Be aware of Streamlit Cloud's free tier limitations

## Free Tier Limitations

Streamlit Cloud free tier includes:
- 1 GB of memory
- 1 dedicated CPU
- Unlimited public apps
- Apps sleep after 7 days of inactivity

## Support

- **Streamlit Cloud:** [Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- **Streamlit Community:** [Forum](https://discuss.streamlit.io/)
- **OpenRouter:** [Documentation](https://openrouter.ai/docs)

## Additional Features to Consider

Once deployed, you might want to add:
- Analytics tracking
- User feedback forms
- Rate limiting
- Caching for improved performance
- Additional AI models or features
- Custom domain (available on paid plans)
