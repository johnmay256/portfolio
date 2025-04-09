import sys
import os

project_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Project {num} - John's Prop Builds</title>
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="portfolio.html">Portfolio</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <h1>Project {num}: Description Here</h1>
    <div class="project-gallery">
      <a href="#img{num}a" class="lightbox-link">
        <img src="images/project{num}-1.jpg" alt="Project {num} - Image 1" />
      </a>
      <a href="#img{num}b" class="lightbox-link">
        <img src="images/project{num}-2.jpg" alt="Project {num} - Image 2" />
      </a>
    </div>

    <div id="img{num}a" class="lightbox">
      <a href="project{num}.html" class="close">&times;</a>
      <img src="images/project{num}-1.jpg" alt="Project {num} - Image 1" />
      <a href="#img{num}b" class="nav-arrow next">&rarr;</a>
      <a href="#img{num}b" class="nav-arrow prev">&larr;</a>
    </div>

    <div id="img{num}b" class="lightbox">
      <a href="project{num}.html" class="close">&times;</a>
      <img src="images/project{num}-2.jpg" alt="Project {num} - Image 2" />
      <a href="#img{num}a" class="nav-arrow prev">&larr;</a>
      <a href="#img{num}a" class="nav-arrow next">&rarr;</a>
    </div>
  </main>

  <footer>
    <p>&copy; 2025 John’s Prop Builds</p>
  </footer>

  <script src="js/hammer.min.js"></script>
  <script src="js/lightbox-swipe.js"></script>
</body>
</html>
'''

portfolio_entry = '''
      <div class="project">
        <a href="project{num}.html">
          <img src="images/project{num}-thumb.jpg" alt="Project {num}">
        </a>
        <p>Project {num} description</p>
      </div>
'''

def generate_project_page(project_number):
    content = project_template.format(num=project_number)
    filename = f"project{project_number}.html"
    with open(filename, "w") as f:
        f.write(content)
    print(f"Created {filename}")

def update_portfolio_html(project_number):
    entry = portfolio_entry.format(num=project_number)
    try:
        with open("portfolio.html", "r") as f:
            lines = f.readlines()

        # Find insertion point before closing </div> of class portfolio-grid
        insert_index = next(i for i, line in enumerate(lines) if '</div>' in line and 'portfolio-grid' in lines[i-1])
        lines.insert(insert_index, entry + '\n')

        with open("portfolio.html", "w") as f:
            f.writelines(lines)
        print("Updated portfolio.html")
    except Exception as e:
        print(f"Error updating portfolio.html: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_project_page_and_update_portfolio.py [project_number]")
    else:
        num = sys.argv[1]
        generate_project_page(num)
        update_portfolio_html(num)
