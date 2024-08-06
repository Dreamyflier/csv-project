import matplotlib
matplotlib.use('Agg')
from django.shortcuts import render, redirect
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import base64
import io


def upload_file(request):
    context = {}
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)

        # Display the first few rows
        context['first_rows'] = df.head().to_html(classes='table table-striped')

        # Calculate summary statistics
        stats = df.describe(include='all').transpose()
        context['summary_stats'] = stats.to_html(classes='table table-striped')

        # Identify and handle missing values
        missing_values = df.isnull().sum()
        context['missing_values'] = missing_values[missing_values > 0].to_frame(name='Missing Values').to_html(classes='table table-striped')

        # Generate histograms for numerical columns
        plots = []
        for column in df.select_dtypes(include=['number']).columns:
            plt.figure(figsize=(8, 4))
            sns.histplot(df[column].dropna(), kde=False)
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')

            # Save plot to a PNG image
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            buffer.seek(0)
            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plots.append(img_str)

        context['plots'] = plots

    return render(request, 'upload.html', context)



