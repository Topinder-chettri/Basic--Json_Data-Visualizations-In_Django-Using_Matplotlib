import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import *
import json


def upload_json(request):
    if request.method == 'POST':
        file = request.FILES['file']
        data = json.loads(file.read().decode('utf-8'))
        JSONData.objects.create(file=file, data=data)
    return render(request, 'temp/upload.html')



def chart(request):
    # Get the JSON data
    data = JSONData.objects.first().data
    # Parse the JSON data
    

    # Process the data to extract the values you want to visualize
    x = [d['country'] for d in data]

    # Generate a scatter plot of the data
    plt.figure(figsize=(13,13))
    plt.plot(x,'ro',color= 'orange',)
    plt.title('country')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Save the plot to a file
    file = "visualize/static/images/chart.png"
    plt.savefig(file)

    # Render the chart in a template
    return render(request, 'temp/visual_chart.html', {'chart': file})
    


def chart1(request):
    # Get the JSON data
    data = JSONData.objects.first().data
    # Parse the JSON data
    

    # Process the data to extract the values you want to visualize
    x = [d['intensity'] for d in data]

    # Generate a scatter plot of the data
    plt.figure(figsize=(13,13))
    plt.plot(x,'ro',color= 'red',)
    plt.title('Intensity')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Save the plot to a file
    file = "visualize/static/images/chart1.png"
    plt.savefig(file)

    # Render the chart in a template
    return render(request, 'temp/visual_chart1.html', {'chart': file})



def chart2(request):
    # Get the JSON data
    data = JSONData.objects.first().data
    # Parse the JSON data
    

    # Process the data to extract the values you want to visualize
    x = [d['likelihood'] for d in data]

    # Generate a scatter plot of the data
    plt.figure(figsize=(13,13))
    plt.plot(x,'ro',color= 'green',)
    plt.title('Likelihood')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Save the plot to a file
    file = "visualize/static/images/chart2.png"
    plt.savefig(file)

    # Render the chart in a template
    return render(request, 'temp/visual_chart2.html', {'chart': file})


def chart3(request):
    # Get the JSON data
    data = JSONData.objects.first().data
    # Parse the JSON data
    

    # Process the data to extract the values you want to visualize
    x = [d['relevance'] for d in data]

    # Generate a scatter plot of the data
    plt.figure(figsize=(13,13))
    plt.plot(x,'ro',color= 'green',)
    plt.title('Relevance')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Save the plot to a file
    file = "visualize/static/images/chart3.png"
    plt.savefig(file)

    # Render the chart in a template
    return render(request, 'temp/visual_chart3.html', {'chart': file})


def chart4(request):
    # Get the JSON data
    data = JSONData.objects.first().data
    # Parse the JSON data
    

    # Process the data to extract the values you want to visualize
    x = [d['topic'] for d in data]

    # Generate a scatter plot of the data
    plt.figure(figsize=(13,20))
    plt.plot(x,'ro',color= 'pink',)
    plt.title('Topic')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Save the plot to a file
    file = "visualize/static/images/chart4.png"
    plt.savefig(file)

    # Render the chart in a template
    return render(request, 'temp/visual_chart4.html', {'chart': file})


def chart5(request):
    # Get the JSON data
    data = JSONData.objects.first().data
    # Parse the JSON data
    

    # Process the data to extract the values you want to visualize
    x = [d['region'] for d in data]

    # Generate a scatter plot of the data
    plt.figure(figsize=(13,20))
    plt.plot(x,'ro',color= 'blue',)
    plt.title('Region')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Save the plot to a file
    file = "visualize/static/images/chart5.png"
    plt.savefig(file)

    # Render the chart in a template
    return render(request, 'temp/visual_chart5.html', {'chart': file})



