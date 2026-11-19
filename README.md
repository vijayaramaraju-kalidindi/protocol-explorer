# Protocol Explorer 🌐

An interactive, visual learning application that animates how internet protocols work packet by packet, with byte-level frame decoding.

## 🚀 Features

- **Interactive Packet Lifecycles**: Step through protocol exchanges in real-time.
- **Multilingual Support**: Supports 20+ languages out of the box.
- **Zero-Dependency Static Architecture**: Pure client-side web application — blazing fast, highly secure, and instant to deploy on Vercel.
- **Customized Branding**: Configured with your own name and profile links.

---

## 🛠️ Local Development

You can run the application locally using Python or Node.js:

### Option 1: Python
```bash
python -m http.server 3000
```
Then visit `http://localhost:3000` in your browser.

### Option 2: Node.js (npx serve)
```bash
npx serve . -p 3000
```

---

## ✏️ Customizing Your Information

A Python script `customize.py` is included to quickly update your branding, social handle, and URLs:

```bash
python customize.py "<Your Full Name>" "<Your Handle>" "<Your Profile URL>" "<Your Vercel App URL>"
```

### Example:
```bash
python customize.py "Vijay Kalidindi" "vijayaramaraju" "https://github.com/vijayaramaraju-kalidindi" "https://protocol-explorer.vercel.app"
```

This updates `index.html`, `sitemap.xml`, `robots.txt`, main script credits, and all 20 translation files automatically.

---

## 🚢 Deploying to Vercel

### Method 1: Using the Vercel CLI

1. Log in to your Vercel account:
   ```bash
   vercel login
   ```
2. Deploy to production:
   ```bash
   vercel --prod
   ```

### Method 2: Deploying via GitHub (Recommended for CI/CD)

1. Initialize git and commit:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of Protocol Explorer twin"
   ```
2. Create a new repository on your GitHub account and push:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<your-username>/protocol-explorer.git
   git push -u origin main
   ```
3. Go to [vercel.com/new](https://vercel.com/new), select your repository, keep all default settings (Framework Preset: **Other** / Root Directory: `./`), and click **Deploy**.
