import os

nav_links = [
    ('index.html', 'Home'),
    ('kitchen.html', 'Kitchen'),
    ('home.html', 'Home Essentials'),
    ('smart.html', 'Smart Gadgets'),
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
          <h3>Categories</h3>
          <ul>
            <li><a href="kitchen.html">Kitchen Gadgets</a></li>
            <li><a href="home.html">Home Essentials</a></li>
            <li><a href="smart.html">Smart Gadgets</a></li>
          </ul>
        </div>
        <div>
          <h3>Quick Links</h3>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="contact.html">Contact Us</a></li>
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

def make_product_card(img_id, title, desc, price):
    return f'''
        <article class="product-card">
          <img src="https://picsum.photos/400/300?random={img_id}" alt="Product" class="product-img">
          <div class="product-content">
            <h3 class="product-title">{title}</h3>
            <p class="product-desc">{desc}</p>
            <div class="product-footer">
              <span class="product-price">${price}</span>
              <a href="contact.html" class="btn btn-outline">View Details</a>
            </div>
          </div>
        </article>'''

# 1. INDEX PAGE
index_content = f'''
  <main>
    <section class="hero">
      <div class="container">
        <h1>Transform Your Home Experience</h1>
        <p>Discover our curated collection of premium home and kitchen gadgets designed to make your life easier and more efficient.</p>
        <a href="kitchen.html" class="btn btn-primary" style="margin-right:1rem;">Explore Collection</a>
        <a href="about.html" class="btn btn-outline">Learn More</a>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-title">
          <h2>Featured Categories</h2>
          <p>Browse our top-rated product categories to find exactly what you need for a modern home.</p>
        </div>
        <div class="grid-3">
          <div class="card">
            <div class="card-icon">🍳</div>
            <h3>Kitchen Gadgets</h3>
            <p>Innovative tools for everyday cooking.</p>
            <a href="kitchen.html" class="btn btn-outline" style="margin-top:1rem;">Shop Now</a>
          </div>
          <div class="card">
            <div class="card-icon">🏠</div>
            <h3>Home Essentials</h3>
            <p>Everything you need for a comfortable living space.</p>
            <a href="home.html" class="btn btn-outline" style="margin-top:1rem;">Shop Now</a>
          </div>
          <div class="card">
            <div class="card-icon">📱</div>
            <h3>Smart Gadgets</h3>
            <p>Automate your home with cutting-edge tech.</p>
            <a href="smart.html" class="btn btn-outline" style="margin-top:1rem;">Shop Now</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section bg-light">
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

    <section class="section">
      <div class="container">
        <div class="section-title">
          <h2>Customer Reviews</h2>
        </div>
        <div class="grid-3">
          <div class="card" style="text-align:left;">
            <p style="font-style:italic;">"The smart kitchen scale I bought is amazing. It connects instantly to my phone. Highly recommend HomeEase!"</p>
            <h4 style="margin-bottom:0; margin-top:1rem;">- Sarah J.</h4>
            <span style="color:#ffc107;">★★★★★</span>
          </div>
          <div class="card" style="text-align:left;">
            <p style="font-style:italic;">"Excellent customer service and fast shipping. The home essentials collection has exactly what I was looking for."</p>
            <h4 style="margin-bottom:0; margin-top:1rem;">- Michael T.</h4>
            <span style="color:#ffc107;">★★★★★</span>
          </div>
          <div class="card" style="text-align:left;">
            <p style="font-style:italic;">"I have automated my entire living room using their smart gadgets. Great prices and reliable products."</p>
            <h4 style="margin-bottom:0; margin-top:1rem;">- David L.</h4>
            <span style="color:#ffc107;">★★★★★</span>
          </div>
        </div>
      </div>
    </section>
  </main>
'''
build_page('index.html', 'Premium Home & Kitchen Gadgets', 'Shop premium home and kitchen gadgets at HomeEase Gadgets.', index_content)


# Category Generator Function
def generate_category_page(filename, title, desc, prefix, start_id):
    cards = ""
    for i in range(1, 13):
        cards += make_product_card(start_id + i, f'{prefix} Product {i}', 'A high-quality, durable gadget that makes daily tasks a breeze. Built with premium materials.', f'{29.99 + i*5:.2f}')
    
    content = f'''
  <div class="page-header">
    <div class="container">
      <h1>{title}</h1>
    </div>
  </div>
  <main class="section">
    <div class="container">
      <div class="grid-4">
        {cards}
      </div>
    </div>
  </main>
'''
    build_page(filename, title, desc, content)

# 2. KITCHEN PAGE
generate_category_page('kitchen.html', 'Kitchen Gadgets', 'Browse our collection of innovative kitchen gadgets.', 'Premium Kitchen', 100)

# 3. HOME ESSENTIALS PAGE
generate_category_page('home.html', 'Home Essentials', 'Shop essential items for a comfortable home.', 'Modern Home', 200)

# 4. SMART GADGETS PAGE
generate_category_page('smart.html', 'Smart Gadgets', 'Discover smart gadgets to automate your life.', 'Smart Tech', 300)


# 5. ABOUT PAGE
about_content = '''
  <div class="page-header">
    <div class="container">
      <h1>About Us</h1>
    </div>
  </div>
  <main class="container">
    <div class="content-box">
      <h2>Our Story</h2>
      <p>Welcome to HomeEase Gadgets. We started with a simple vision: to bring innovative, high-quality, and aesthetically pleasing products into every home. What began as a small passion project has grown into a trusted destination for thousands of homeowners seeking to elevate their daily routines.</p>
      
      <h2>Our Mission</h2>
      <p>Our mission is to simplify your life through technology and smart design. We carefully curate our collection to ensure that every product we feature meets strict standards for durability, functionality, and style.</p>
      
      <h2>Our Vision</h2>
      <p>We envision a future where everyday tasks are effortless, allowing you to spend more time on what truly matters: family, hobbies, and relaxation.</p>
      
      <h2>Our Values</h2>
      <ul>
        <li><strong>Quality First:</strong> We never compromise on the materials or build of our products.</li>
        <li><strong>Customer Centric:</strong> Your satisfaction is the driving force behind everything we do.</li>
        <li><strong>Innovation:</strong> We are constantly searching for the next big thing in home technology.</li>
      </ul>
      
      <h2>Why Choose Us?</h2>
      <p>With thousands of 5-star reviews, secure checkout, and a dedicated support team, HomeEase Gadgets is your reliable partner in creating a modern, comfortable living space. Join our community today and experience the difference.</p>
    </div>
  </main>
'''
build_page('about.html', 'About Us', 'Learn more about the mission and vision of HomeEase Gadgets.', about_content)


# 6. CONTACT PAGE
contact_content = '''
  <div class="page-header">
    <div class="container">
      <h1>Contact Us</h1>
    </div>
  </div>
  <main class="container">
    <div class="content-box">
      <div class="grid-3" style="grid-template-columns: 1fr 1fr; gap: 4rem;">
        
        <div>
          <h2>Get In Touch</h2>
          <p>Have a question about a product, your order, or just want to say hi? Fill out the form or use our contact details below.</p>
          
          <div style="margin-top:2rem;">
            <p><strong>Address:</strong><br>456 Innovation Drive<br>Tech Park, CA 90210</p>
            <br>
            <p><strong>Phone:</strong><br>+1 (555) 987-6543</p>
            <br>
            <p><strong>Email:</strong><br>support@homeeasegadgets.com</p>
            <br>
            <p><strong>Business Hours:</strong><br>Mon-Fri: 9:00 AM - 6:00 PM (PST)<br>Sat-Sun: Closed</p>
          </div>
        </div>

        <div>
          <form style="display:flex; flex-direction:column; gap:1rem; margin-top:2rem;" onsubmit="event.preventDefault(); alert('Message sent successfully!');">
            <div class="form-group">
              <label class="form-label" for="name">Full Name</label>
              <input type="text" id="name" class="form-control" placeholder="John Doe" required>
            </div>
            <div class="form-group">
              <label class="form-label" for="email">Email Address</label>
              <input type="email" id="email" class="form-control" placeholder="john@example.com" required>
            </div>
            <div class="form-group">
              <label class="form-label" for="message">Your Message</label>
              <textarea id="message" class="form-control" rows="5" placeholder="How can we help you?" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%;">Send Message</button>
          </form>
        </div>

      </div>
      
      <div style="margin-top: 4rem; background:#eee; height:350px; display:flex; align-items:center; justify-content:center; color:#888; border-radius:8px;">
        [ Embedded Google Maps Placeholder ]
      </div>
    </div>
  </main>
'''
build_page('contact.html', 'Contact Us', 'Get in touch with the HomeEase Gadgets support team.', contact_content)


# 7. PRIVACY POLICY PAGE
privacy_content = '''
  <div class="page-header">
    <div class="container">
      <h1>Privacy Policy</h1>
    </div>
  </div>
  <main class="container">
    <div class="content-box">
      <p><strong>Effective Date:</strong> October 12, 2026</p>
      
      <h2>1. Information We Collect</h2>
      <p>We collect information you provide directly to us, such as when you create an account, subscribe to our newsletter, or contact customer support. This may include your name, email address, and browsing data.</p>
      
      <h2>2. How We Use Your Information</h2>
      <p>We use the information we collect to operate, maintain, and improve our website. We may also use it to communicate with you, process transactions, and send promotional materials.</p>
      
      <h2>3. Cookies and Tracking Technologies</h2>
      <p>HomeEase Gadgets uses cookies to enhance your browsing experience. Cookies are small data files stored on your device that help us analyze site traffic and remember your preferences.</p>
      
      <h2>4. Third-Party Links</h2>
      <p>Our website may contain links to third-party websites or affiliate partners. We are not responsible for the privacy practices or content of these external sites.</p>
      
      <h2>5. Security</h2>
      <p>We implement reasonable security measures to protect your personal information. However, no method of transmission over the Internet is 100% secure.</p>
      
      <h2>6. Contact Us</h2>
      <p>If you have any questions about this Privacy Policy, please contact us at support@homeeasegadgets.com.</p>
    </div>
  </main>
'''
build_page('privacy-policy.html', 'Privacy Policy', 'Privacy Policy for HomeEase Gadgets.', privacy_content)


# 8. TERMS & CONDITIONS PAGE
terms_content = '''
  <div class="page-header">
    <div class="container">
      <h1>Terms & Conditions</h1>
    </div>
  </div>
  <main class="container">
    <div class="content-box">
      <p><strong>Effective Date:</strong> October 12, 2026</p>
      
      <h2>1. Website Usage</h2>
      <p>By accessing and using HomeEase Gadgets, you agree to comply with and be bound by these Terms & Conditions. If you do not agree, please do not use our website.</p>
      
      <h2>2. Intellectual Property</h2>
      <p>All content on this website, including text, graphics, logos, and images, is the property of HomeEase Gadgets or its content suppliers and is protected by intellectual property laws. You may not reproduce or distribute our content without written permission.</p>
      
      <h2>3. External Links</h2>
      <p>This website may include links to external websites for your convenience. We have no control over the nature, content, and availability of those sites. The inclusion of any links does not necessarily imply a recommendation or endorse the views expressed within them.</p>
      
      <h2>4. Disclaimer of Warranties</h2>
      <p>This website and its content are provided "as is" without any warranties of any kind, either express or implied. We do not warrant that the site will be available, secure, or error-free.</p>
      
      <h2>5. Limitation of Liability</h2>
      <p>In no event shall HomeEase Gadgets be liable for any direct, indirect, incidental, consequential, or punitive damages arising out of your use of, or inability to use, this website.</p>
    </div>
  </main>
'''
build_page('terms.html', 'Terms & Conditions', 'Terms & Conditions for using HomeEase Gadgets.', terms_content)


# 9. DISCLAIMER PAGE
disclaimer_content = '''
  <div class="page-header">
    <div class="container">
      <h1>Disclaimer</h1>
    </div>
  </div>
  <main class="container">
    <div class="content-box">
      <h2>Informational Purposes Only</h2>
      <p>The content provided on HomeEase Gadgets is for general informational and educational purposes only. While we strive to keep the information up to date and correct, we make no representations or warranties of any kind regarding the completeness, accuracy, reliability, or suitability of the products reviewed or featured.</p>
      
      <h2>Affiliate Disclosure</h2>
      <p>HomeEase Gadgets is a participant in various affiliate marketing programs. This means that we may earn a commission on purchases made through our links to retailer sites, at no additional cost to you.</p>
      
      <h2>Product Information</h2>
      <p>We do not manufacture or directly sell the products listed on this website. Prices, availability, and product specifications are subject to change without notice by the respective manufacturers or retailers.</p>
      
      <h2>User Responsibility</h2>
      <p>It is the user's responsibility to verify all product information, read actual customer reviews, and check retailer policies before making any purchasing decisions. We cannot be held liable for any dissatisfaction or issues arising from products purchased via third-party links.</p>
    </div>
  </main>
'''
build_page('disclaimer.html', 'Disclaimer', 'Legal Disclaimer and Affiliate Disclosure for HomeEase Gadgets.', disclaimer_content)

print("HomeEase Gadgets built successfully.")
