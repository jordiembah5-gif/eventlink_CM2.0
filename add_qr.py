with open('EventLink CM Project/frontend/user-home.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'qrserver' not in html:
    html = html.replace(
        '<h4 style="margin-bottom: 3px;">${event.name}</h4>',
        '<h4 style="margin-bottom: 3px;">${event.name}</h4><p style="font-size: 11px; color: #0071E3; font-weight: 600; margin-bottom: 2px;"><i class="fas fa-qrcode"></i> QR Ticket Ready</p>'
    )
    
    search_str = '</div>\n                              <div>\n                                  <h4'
    replace_str = '</div>\n                              <div style="margin-right: 15px;">\n                                  <img src="https://api.qrserver.com/v1/create-qr-code/?size=60x60&data=${currentUserEmail}-${event.id}" alt="QR" style="border-radius: 4px; border: 1px solid #ddd; padding: 2px;">\n                              </div>\n                              <div>\n                                  <h4'
    html = html.replace(search_str, replace_str)

    with open('EventLink CM Project/frontend/user-home.html', 'w', encoding='utf-8') as f:
        f.write(html)
