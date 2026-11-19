import os
import re

def customize_project(
    name="Vijay Kalidindi",
    handle="vijayaramaraju",
    profile_url="https://github.com/vijayaramaraju-kalidindi",
    app_url="https://protocol-explorer.vercel.app",
    project_dir=r"c:\Vj_Data\Study\Protocol Explorer"
):
    print(f"Applying customizations:")
    print(f"  Name: {name}")
    print(f"  Handle: {handle}")
    print(f"  Profile URL: {profile_url}")
    print(f"  App URL: {app_url}")

    # 1. Update index.html
    index_html_path = os.path.join(project_dir, "index.html")
    if os.path.exists(index_html_path):
        with open(index_html_path, "r", encoding="utf-8") as f:
            html = f.read()

        html = html.replace('content="Dilum Sanjaya"', f'content="{name}"')
        html = html.replace('content="@DilumSanjaya"', f'content="@{handle}"')
        html = html.replace('"name": "Dilum Sanjaya"', f'"name": "{name}"')
        html = html.replace('"url": "https://x.com/DilumSanjaya"', f'"url": "{profile_url}"')
        html = html.replace('https://protocol-explorer-alpha.vercel.app', app_url)

        with open(index_html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Updated index.html")

    # 2. Update sitemap.xml & robots.txt
    sitemap_path = os.path.join(project_dir, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap = f.read()
        sitemap = sitemap.replace('https://protocol-explorer-alpha.vercel.app', app_url)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(sitemap)
        print("Updated sitemap.xml")

    robots_path = os.path.join(project_dir, "robots.txt")
    if os.path.exists(robots_path):
        with open(robots_path, "r", encoding="utf-8") as f:
            robots = f.read()
        robots = robots.replace('https://protocol-explorer-alpha.vercel.app', app_url)
        with open(robots_path, "w", encoding="utf-8") as f:
            f.write(robots)
        print("Updated robots.txt")

    # 3. Update assets/index-CNPseYOQ.js
    main_js_path = os.path.join(project_dir, "assets", "index-CNPseYOQ.js")
    if os.path.exists(main_js_path):
        with open(main_js_path, "r", encoding="utf-8") as f:
            js = f.read()

        js = js.replace('https://x.com/DilumSanjaya', profile_url)
        js = js.replace('Dilum Sanjaya on X', f'{name} on Profile')
        js = js.replace('DilumSanjaya', handle)

        with open(main_js_path, "w", encoding="utf-8") as f:
            f.write(js)
        print("Updated assets/index-CNPseYOQ.js")

    # 4. Update all translation JS chunks in assets/
    assets_dir = os.path.join(project_dir, "assets")
    for f in os.listdir(assets_dir):
        if f.endswith(".js") and f != "index-CNPseYOQ.js":
            p = os.path.join(assets_dir, f)
            with open(p, "r", encoding="utf-8") as fp:
                c = fp.read()
            if "Dilum Sanjaya" in c:
                # Replace key and localized text
                c = c.replace("Dilum Sanjaya on X", f"{name} on Profile")
                c = c.replace("Dilum Sanjaya", name)
                with open(p, "w", encoding="utf-8") as fp:
                    fp.write(c)
                print(f"Updated localization chunk: {f}")

    print("\nCustomization complete!")

if __name__ == "__main__":
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "Vijay Kalidindi"
    handle = sys.argv[2] if len(sys.argv) > 2 else "vijayaramaraju"
    profile_url = sys.argv[3] if len(sys.argv) > 3 else "https://github.com/vijayaramaraju-kalidindi"
    app_url = sys.argv[4] if len(sys.argv) > 4 else "https://protocol-explorer.vercel.app"
    customize_project(name, handle, profile_url, app_url)
