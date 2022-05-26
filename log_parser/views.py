from django.shortcuts import render
from .forms import LogUpload
import re
from collections import Counter


# Create your views here.
def log_parser_index(request):
    if request.method == 'POST':
        form = LogUpload(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file'].read()
            txt = str(f.decode('utf-8'))
            pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            ips = re.findall(pattern, txt)

            result = Counter(ips).most_common(10)  # список кортежей из двух элементов

            ban = []
            for key, value in result:
                if value > 10:
                    ban.append({'ip': key,
                                'frequency': value})
            print(ban)
            return render(request, 'log_parser/parser_index.html', {'form': form, 'ips': ban})

    else:
        form = LogUpload()

    return render(request, 'log_parser/parser_index.html', {'form': form})
