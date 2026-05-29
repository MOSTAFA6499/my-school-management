g: 5px 12px; border-radius: 8px;">❌ حذف</a>
            </div>
            {% else %}
            <p style="text-align: center; color: #999;">هیچ {{ role_name }}ای ثبت نشده است.</p>
            {% endfor %}
        </div>
        
        <div class="footer">
            سیستم مدیریت آموزشگاه | همه نقش‌ها در یک جا
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    tab = request.args.get('tab', 'starters')
    current_tab = tab
    
    role_names = {
        'leaders': 'لیدر',
        'managers': 'منیجر',
        'presentors': 'پرزنتر',
        'starters': 'شروع کننده'
    }
    
    if request.method == 'POST':
        name = request.form['name']
        family = request.form['family']
        phone = request.form['phone']
        specialty = request.form['specialty']
        
        new_person = {
            'name': name,
            'family': family,
            'phone': phone,
            'specialty': specialty
        }
        
        if current_tab == 'leaders':
            leaders.append(new_person)
        elif current_tab == 'managers':
            managers.append(new_person)
        elif current_tab == 'presentors':
            presentors.append(new_person)
        else:
            starters.append(new_person)
        
        return redirect(url_for('index', tab=current_tab))
    
    items = []
    if current_tab == 'leaders':
        items = leaders
    elif current_tab == 'managers':
        items = managers
    elif current_tab == 'presentors':
        items = presentors
    else:
        items = starters
    
    return render_template_string(HTML_TEMPLATE, 
                                 leaders=leaders,
                                 managers=managers,
                                 presentors=presentors,
                                 starters=starters,
                                 current_tab=current_tab,
                                 role_name=role_names.get(current_tab, ''),
                                 items=items)

@app.route('/delete/<tab>/<int:index>')
def delete(tab, index):
    if tab == 'leaders' and 0 <= index < len(leaders):
        leaders.pop(index)
    elif tab == 'managers' and 0 <= index < len(managers):
        managers.pop(index)
    elif tab == 'presentors' and 0 <= index < len(presentors):
        presentors.pop(index)
    elif tab == 'starters' and 0 <= index < len(starters):
        starters.pop(index)
    return redirect(url_for('index', tab=tab))

if __name__ == '__main__':
    app.run(debug=True)
