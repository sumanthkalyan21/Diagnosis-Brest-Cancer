from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
@csrf_exempt
def index(request):
    if request.method == 'POST':
        Radius = request.post.get('Radius')
        Texture = request.POST.get('Texture')
        Perimeter = request.POST.get('Perimeter')
        Area = request.POST.get('Area')
        df = pd.read_csv('data.csv')
        X = df.drop[['Radius_mean','Texture_mean','Perimeter_mean','Area_mean']]
        y = df['Diagnosis']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=10)
        from sklearn.svm import SVC
        svs = SVC(kernel='linear')
        svs.fit(X_train, y_train)
        y_pred = svs.predict(X_test)
        new = {'Radius': [123],
               'Texture': [121],
               'Perimeter': [122],
               'Area': [111]
               }
        new['Radius'][0] = float(Radius)
        new['Texture'][0] = float(Texture)
        new['Perimeter'][0] = float(Perimeter)
        new['Area'][0] = int(Area)
        df2 = pd.dataframe(new, columns=['Radius', 'Texture','Perimeter','Area'])
        y_pred = svs.predict(df2)
        name=str(y_pred[0])
        context = {
            'name' : name,
        }
        template = loader.get_template('shwdta.html')
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('indx.html')
        return HttpResponse(template.render())