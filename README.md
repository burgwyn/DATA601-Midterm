# DATA601-Midterm

## Overview

School performance reporting has existed for some time, seeking to assess and quantify the effectiveness of public school systems.  Often, these assessments look solely at student achievement through results of standardized tests.  The source data set and this analysis are novel because of the features under review which extend beyond simply test scores and include a holistic, 360 degree view of the school's experience.

Chicago is among the nation's largest public school districts spanning a large population with differing economic conditions.  While the source dataset doesn't explicitly indicate economic terms, it does include score for safety and parent support which serve as a proxy for economic conditions.

The dataset captures a range of factors: attendance, instruction, parental support, safety and geography. This analysis is a review these different factors and identify which features are representative of a high achieving school. 

## Goals

- Identify the traits that factor into a superlative school
- Determine if geographic factors have any impact on school performance
- Create a model that scores 85% or better

## Motivation & Background

I'm interested in open government and open data and I want to better understand the services offered to citizens.  I am a former Chicago resident and this dataset overlaps with my last year in the city.

My mother was an educator, as is my mother-in-law.  I'm also the father of kindergarteners, so understanding how to identify the traits of good schools is of personal interest.

School performance metrics like these have been published in other school districts, but I was unable to find studies or Chicago Public Schools and this data set.  Additionally, the format of these reports have changed in subsequent years.

## Data

The data set under review is [Chicago Public Schools - Progress Report Cards (2011-2012)](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t) as published in the City of Chicago's [Data Portal](https://data.cityofchicago.org/).

The data set includes reporting data for all schools in the Chicago Public School system regardless of level, ie Elementary, Middle or High schools.

There is a published [data dictionary](https://data.cityofchicago.org/api/assets/AAD41A13-BE8A-4E67-B1F5-86E711E09D5F) and below are are subset, specifically the features under review.

ADEQUATE YEARLY PROGRESS MADE: Binary value establishing if the school is meeting performance goals
SAFETY SCORE: Student Perception/Safety score from 5 Essentials survey
FAMILY INVOLVEMENT SCORE: Involved Families score from 5 Essentials survey
ENVIRONMENT SCORE: Supportive Environment score from 5 Essentials survey
INSTRUCTION SCORE: Ambitious Instruction score from 5 Essentials survey
LEADERS SCORE: Effective Leaders score from 5 Essentials survey
TEACHERS SCORE: Collaborative Teachers score from 5 Essentials survey
PARENT ENGAGEMENT SCORE: Parent Perception/Engagement score from parent survey
AVERAGE STUDENT ATTENDANCE: Average daily student attendance
RATE OF MISCONDUCTS (PER 100 STUDENTS): # of misconducts per 100 students
AVERAGE TEACHER ATTENDANCE: Average daily teacher attendance
INDIVIDUALIZED EDUCATION PROGRAM COMPLIANCE RATE: % of IEPs and 504 plans completed by due date
COLLEGE ENROLLMENT (NUMBER OF STUDENTS): Total school enrollment
WARD: City's ward where the school is located
POLICE DISTRICT: Police unit assigned the school's location

## Table of Contents

## Packages and Software

Project Info
Contributors: Nat Burgwyn

Languages: Python

Tools: PyCharm, Jupyter Notebook

Libraries: pandas, sklearn, matplotlib, seaborn
