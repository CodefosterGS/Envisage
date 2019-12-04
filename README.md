# Envisage


    The idea is to create a web application which performs the following actions:
    
    1. User Can upload files of following types: 
        a. Text 
        b. Excel 
        c. CSV 
        d. Image 
          i. JPG
          ii. PNG 
          iii. GIF 
        e. Video 
          i. MP4 
    2. Once the file is uploaded, on the basis of file types, the system should display analytics 
        about the data present in the file 
    3. For Text based file 
        a. Tokens of words and characters 
        b. TF and IDF of various words 
        c. Option to download corpus 
        d. Option to download semantic tree as an image 
    4. For Excel and CSV 
        a. Generate table on webpage with the data and option to perform a search on any 
            one of the columns 
    5. Image 
        a. RGB Desegregation of image, i.e. generate three images separately showing 
            only red, blue and green pixels in the image respectively 
        b. Dimension of image 
    6. Video 
        a. Frame desegregation of video and show images that formed the video with an 
            option to download individual images 
        b. Provide option for user to apply mask on video and download the processed video 
        c. Crop the video and download it 

    
    
Goals

    To visualize a file containing certain text and downloadable parse tree of text.
    To desegrate image based on rbg and downloadable images with processing of the same.
    To denerate a maskable video which is downloadable
    To visualise table of csv and Excel format and apply search on different columns
    
Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
Requirements

    Any operating system (i.e. Linux, Windows, MacOS X)
    A knowledge of Python and little knowledge of image,video and text processing. Don't worry if you are new to it, you just need knack to learn.

Development Setup

The development environment requires a linux system with Python 3.6 and clone of the forked version of this repository.
Setting up the project


    Install Python

        https://realpython.com/installing-python/

    Installing Flask
    
        https://pypi.org/project/Flask/
        
    
Schedule
Sprint I

    Look over the project and read the goals to be met for project.
    Learn and Reasearch on text processing,image processing,video processing(python).
    
Sprint II

    Taking different sprint for text, image,Excel/CSV and video and implementing the functionalities of them respectively.

Phase III

    Testing of all functionlities with different files. 
    
    
Contribution Guidelines

Please raise a feature request or issue before sending PR for the same.

Follow the below guidelines for proper coding practices:

    Always create a new branch for your changes and make PR from it ONLY.
    Write neat code with proper comments.
    Follow PEP8 coding style.
    Write descriptive commit messages. Please read this for more information.
    Write detailed PR messages and include fixes #ISSUE_NUMBER it if closes an issue, otherwise use concerns #ISSUE_NUMBER to tag the related issues. Please refer here for more PR guidelines.
    It is recommended to have a single commit for a task.
    Use DRY principles to create maintainable code.

Contributing

You can contribute in several ways. If you know how to code or are a designer, you are welcome to contribute using pull requests. You can also contribute by opening issues about defects and things that could be improved or request entirely new features that you think would help others. Join the Slack Communication Channel

Mentors

    Soham Chhapre
    Aatmik Jain

License

This project is licensed under the Codefoster and SGSITS.
