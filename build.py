import os

nav_links = [
    ('index.html', 'Home'),
    ('products.html', 'Products'),
    ('about.html', 'About'),
    ('contact.html', 'Contact')
]

def make_nav(current_page):
    nav = ""
    for filename, title in nav_links:
        active = ' class="active"' if current_page == filename else ''
        nav += f'<a href="{filename}"{active}>{title}</a>\n        '
    return nav.strip()

def make_header(current_page):
    return f'''  <header class="header">
    <div class="container header-container">
      <a href="index.html" class="logo">HomeEase Gadgets</a>
      <div class="hamburger">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <nav class="nav-links">
        {make_nav(current_page)}
      </nav>
    </div>
  </header>'''

def make_footer():
    return '''  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <h3>HomeEase Gadgets</h3>
          <p>Your premium destination for modern, innovative, and reliable home and kitchen essentials.</p>
        </div>
        <div>
          <h3>Customer Support</h3>
          <ul>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="about.html">About Us</a></li>
          </ul>
        </div>
        <div>
          <h3>Quick Links</h3>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="products.html">All Products</a></li>
          </ul>
        </div>
        <div>
          <h3>Legal</h3>
          <ul>
            <li><a href="privacy-policy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms & Conditions</a></li>
            <li><a href="disclaimer.html">Disclaimer</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 HomeEase Gadgets. All rights reserved.</p>
      </div>
    </div>
  </footer>
  
  <button id="scrollTopBtn" aria-label="Scroll to top">↑</button>'''

def make_head(title, desc):
    return f'''<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | HomeEase Gadgets</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="css/style.css">
  <style>
    .product-img {{
      object-fit: cover;
      height: 250px;
      width: 100%;
      border-radius: var(--radius) var(--radius) 0 0;
    }}
  </style>
</head>'''

def build_page(filename, title, desc, content):
    html = f'''<!DOCTYPE html>
<html lang="en">
{make_head(title, desc)}
<body>
{make_header(filename)}
{content}
{make_footer()}
  <script src="js/script.js"></script>
</body>
</html>'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

def slugify(text):
    return text.lower().replace(' ', '-')

def make_product_card(title, category, price):
    slug = slugify(title)
    local_img = f"assets/images/{category}/{slug}.jpg"
    desc = f"Premium {title.lower()} designed to bring convenience and elegance to your daily routine."
    
    return f'''
        <article class="product-card card" style="padding:0; overflow:hidden;">
          <img src="{local_img}" alt="{title}" class="product-img" loading="lazy">
          <div class="product-content" style="padding: 1.5rem;">
            <h3 class="product-title">{title}</h3>
            <p class="product-desc" style="flex-grow:1;">{desc}</p>
            <div class="product-footer" style="display:flex; justify-content:space-between; align-items:center; margin-top:1rem;">
              <span class="product-price" style="font-weight:bold; font-size:1.2rem; color:var(--primary-color);">${price}</span>
              <a href="contact.html" class="btn btn-outline">View Details</a>
            </div>
          </div>
        </article>'''

print("Rapidly rebuilding HTML with updated small business structure...")

# 1. INDEX PAGE
index_content = f'''
  <main>
    <section class="hero" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('assets/images/hero.jpg'); background-size: cover; background-position: center; color: white;">
      <div class="container">
        <h1 style="color: white;">Transform Your Home Experience</h1>
        <p style="color: #f0f0f0;">Discover our curated collection of premium home and kitchen gadgets designed to make your life easier and more efficient.</p>
        <a href="products.html" class="btn btn-primary" style="margin-right:1rem;">Explore Collection</a>
        <a href="about.html" class="btn btn-outline" style="border-color: white; color: white;">Learn More</a>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-title">
          <h2>Featured Categories</h2>
        </div>
        <div class="grid-3">
          <div class="card" style="padding: 0; overflow: hidden;">
            <img src="assets/images/kitchen/category.jpg" alt="Kitchen Appliances" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
            <div style="padding: 1.5rem;">
              <h3>Kitchen Appliances</h3>
              <p>Innovative tools for everyday cooking.</p>
              <a href="products.html#kitchen" class="btn btn-outline" style="margin-top:1rem;">Shop Now</a>
            </div>
          </div>
          <div class="card" style="padding: 0; overflow: hidden;">
            <img src="assets/images/home/category.jpg" alt="Home Organization" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
            <div style="padding: 1.5rem;">
              <h3>Home Essentials</h3>
              <p>Everything you need for a comfortable living space.</p>
              <a href="products.html#home" class="btn btn-outline" style="margin-top:1rem;">Shop Now</a>
            </div>
          </div>
          <div class="card" style="padding: 0; overflow: hidden;">
            <img src="assets/images/smart/category.jpg" alt="Smart Home" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
            <div style="padding: 1.5rem;">
              <h3>Smart Home</h3>
              <p>Automate your home with cutting-edge tech.</p>
              <a href="products.html#smart" class="btn btn-outline" style="margin-top:1rem;">Shop Now</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section bg-light">
      <div class="container">
        <div class="section-title">
          <h2>Featured Products</h2>
        </div>
        <div class="grid-3">
            {make_product_card('Air Fryer', 'kitchen', '99.99')}
            {make_product_card('Vacuum Cleaner', 'home', '149.99')}
            {make_product_card('Robot Vacuum', 'smart', '199.99')}
            {make_product_card('Coffee Maker', 'kitchen', '89.99')}
            {make_product_card('Air Purifier', 'home', '129.99')}
            {make_product_card('Smart Doorbell', 'smart', '109.99')}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-title">
          <h2>Why Choose Us</h2>
        </div>
        <div class="grid-4">
          <div style="text-align:center;">
            <h3 style="color:var(--primary-color);">Premium Quality</h3>
            <p>We source only the highest quality materials.</p>
          </div>
          <div style="text-align:center;">
            <h3 style="color:var(--primary-color);">Fast Shipping</h3>
            <p>Reliable and tracked delivery to your door.</p>
          </div>
          <div style="text-align:center;">
            <h3 style="color:var(--primary-color);">Secure Checkout</h3>
            <p>Your payment data is fully encrypted.</p>
          </div>
          <div style="text-align:center;">
            <h3 style="color:var(--primary-color);">24/7 Support</h3>
            <p>Our team is always here to assist you.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section bg-light">
      <div class="container">
        <div class="section-title">
          <h2>Frequently Asked Questions</h2>
        </div>
        <div style="max-width: 800px; margin: 0 auto;">
            <div class="faq-item">
                <h3>Do you ship internationally?</h3>
                <p>Yes, we ship to most countries worldwide. Shipping costs will apply and will be added at checkout.</p>
            </div>
            <div class="faq-item">
                <h3>What is your return policy?</h3>
                <p>We accept returns within 30 days of the original purchase date for items in unused condition.</p>
            </div>
            <div class="faq-item">
                <h3>Are the smart gadgets compatible with Alexa and Google Home?</h3>
                <p>Yes, all our smart gadgets integrate seamlessly with major smart home ecosystems.</p>
            </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="newsletter-box">
          <h2>Join Our Newsletter</h2>
          <p style="margin-bottom: 2rem;">Subscribe to get special offers, free giveaways, and once-in-a-lifetime deals.</p>
          <form style="display:flex; justify-content:center; flex-wrap:wrap; align-items:center;" onsubmit="event.preventDefault(); alert('Subscribed!');">
              <input type="email" placeholder="Enter your email address" required>
              <button type="submit" class="btn btn-outline" style="background:white; color:var(--primary-color); border:2px solid white; margin-bottom:10px;">Subscribe</button>
          </form>
        </div>
      </div>
    </section>
  </main>
'''
build_page('index.html', 'Premium Home & Kitchen Gadgets', 'Shop premium home and kitchen gadgets at HomeEase Gadgets.', index_content)


# 2. PRODUCTS PAGE
def make_category_section(title, category_id, products, category_folder):
    cards = ""
    for i, prod in enumerate(products):
        price = f"{29.99 + i*15:.2f}"
        cards += make_product_card(prod, category_folder, price)
        
    return f'''
    <section id="{category_id}" class="section" style="padding-top: 4rem;">
      <div class="container">
        <div class="section-title">
          <h2>{title}</h2>
        </div>
        <div class="grid-3">
          {cards}
        </div>
      </div>
    </section>
    '''

kitchen_products = ['Air Fryer', 'Blender', 'Coffee Maker', 'Electric Kettle', 'Toaster']
home_products = ['Vacuum Cleaner', 'Storage Organizer', 'Air Purifier', 'Laundry Basket', 'Steam Mop']
smart_products = ['Robot Vacuum', 'Smart Plug', 'Smart LED Bulb', 'Smart Speaker', 'Smart Doorbell']

products_content = f'''
  <div class="page-header">
    <div class="container">
      <h1>All Products</h1>
    </div>
  </div>
  <main>
    {make_category_section("Kitchen Appliances", "kitchen", kitchen_products, "kitchen")}
    <hr style="border:none; border-top:1px solid var(--border-color); max-width:1200px; margin:0 auto;">
    {make_category_section("Home Essentials", "home", home_products, "home")}
    <hr style="border:none; border-top:1px solid var(--border-color); max-width:1200px; margin:0 auto;">
    {make_category_section("Smart Home", "smart", smart_products, "smart")}
  </main>
'''
build_page('products.html', 'All Products', 'Browse all premium home gadgets.', products_content)


# 3. ABOUT PAGE
about_content = f'''
  <div class="page-header">
    <div class="container">
      <h1>About Us</h1>
    </div>
  </div>
  <main class="container">
    <div class="content-box">
      <img src="assets/images/about.jpg" alt="Modern Kitchen Interior" style="width: 100%; height: 400px; object-fit: cover; border-radius: var(--radius); margin-bottom: 2rem;" loading="lazy">
      <h2>Our Story</h2>
      <p>Welcome to HomeEase Gadgets. We started with a simple vision: to bring innovative, high-quality, and aesthetically pleasing products into every home.</p>
    </div>
  </main>
'''
build_page('about.html', 'About Us', 'Learn more about HomeEase Gadgets.', about_content)


# 4. CONTACT PAGE
contact_content = f'''
  <div class="page-header">
    <div class="container">
      <h1>Contact Us</h1>
    </div>
  </div>
  <main class="container">
    <div class="content-box">
      <img src="assets/images/contact.jpg" alt="Customer Support Office" style="width: 100%; height: 300px; object-fit: cover; border-radius: var(--radius); margin-bottom: 2rem;" loading="lazy">
      <div class="grid-3" style="grid-template-columns: 1fr 1fr; gap: 4rem;">
        <div>
          <h2>Get In Touch</h2>
          <p><strong>Address:</strong> 456 Innovation Drive, Tech Park, CA 90210</p>
          <p><strong>Phone:</strong> +1 (555) 987-6543</p>
          <p><strong>Email:</strong> support@homeeasegadgets.com</p>
        </div>
      </div>
    </div>
  </main>
'''
build_page('contact.html', 'Contact Us', 'Get in touch with us.', contact_content)

# Legal Pages
def write_legal_pages():
    privacy_content = '''<div class="page-header"><div class="container"><h1>Privacy Policy</h1></div></div><main class="container"><div class="content-box"><p>Standard privacy policy.</p></div></main>'''
    build_page('privacy-policy.html', 'Privacy Policy', 'Privacy Policy.', privacy_content)
    
    terms_content = '''<div class="page-header"><div class="container"><h1>Terms & Conditions</h1></div></div><main class="container"><div class="content-box"><p>Standard terms.</p></div></main>'''
    build_page('terms.html', 'Terms & Conditions', 'Terms.', terms_content)
    
    disclaimer_content = '''<div class="page-header"><div class="container"><h1>Disclaimer</h1></div></div><main class="container"><div class="content-box"><p>Standard disclaimer.</p></div></main>'''
    build_page('disclaimer.html', 'Disclaimer', 'Disclaimer.', disclaimer_content)

write_legal_pages()
print("HomeEase Gadgets successfully rebuilt.")
