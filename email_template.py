def generate_email_html(subject, summary, precautions):
    html = f"""
    <html>
      <head>
        <style>
          body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 20px;
          }}
          .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
          }}
          h1 {{
            color: #2c3e50;
            padding: 20px;
            margin: 0;
            background-color: #f8f9fa;
            border-bottom: 1px solid #e0e0e0;
          }}
          h2 {{
            color: #3498db;
            margin-top: 20px;
            margin-bottom: 10px;
            padding: 0 20px;
          }}
          p {{
            margin: 10px 0;
            padding: 0 20px;
          }}
          ul {{
            background-color: #f8f9fa;
            margin: 0 20px 20px;
            padding: 15px 20px 15px 40px;
            border-radius: 5px;
          }}
          li {{
            margin-bottom: 10px;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <h1>{subject}</h1>
          <h2>Summary</h2>
          {"".join(f"<p>{line}</p>" for line in summary)}
          <h2>Precautionary Steps</h2>
          <ul>
            {"".join(f"<li>{step}</li>" for step in precautions)}
          </ul>
        </div>
      </body>
    </html>
    """
    return html
