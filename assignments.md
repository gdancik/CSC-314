---
layout: page
title: Assignments 
permalink: /assignments/
order: 3
exclude_from_nav: false
---

{% comment %}
<p style = 'color:red;font-size:104%'>Note: All assignments must be submitted through <a href = "https://easternct.blackboard.com/">Blackboard</a> and are due at the beginning of class (9:00 AM) unless stated otherwise</p>
{% endcomment %}


<style>
.hide {
  display:none;
}

ul {
    margin-bottom: 5px;
}

.due {
    background-color: yellow
}


</style>

{% comment %}
<div id = 'hidden' class = 'hide' markdown="1">
{% endcomment %}

* Watch the You Tube videos covering genes, SNPs, and where your genes come from linked in the <a href = "../notes/">Course Introduction</a> notes
* Install the Anaconda Individual Distribution on your personal computer, by following the Software installation instructions on the [Course Info](../info/) page. We will begin using Python in early February.
<!--<hr style = 'height:1px; background-color:maroon'> -->
* [Lab #1 - OMIM and Inheritance]({{ site.baseurl }}/data/hw/Lab1_OMIM.docx) (Due: Monday, 01/30/2023) 
* [Lab #2 - Python Lab]({{ site.baseurl }}/data/hw/Lab2.ipynb)
(Due: Wednesday, 02/08/2023; submit through [Blackboard](http://easternct.blackboard.com))
* Lab #3 - DNA and complements (Due: Monday, 02/13/2023, submit through [Blackboard](http://easternct.blackboard.com))
    * [Lab #3 DNA Questions]({{ site.baseurl }}/data/hw/Lab3_Complements.docx)
    * [Lab #3 Notebook]({{ site.baseurl }}/data/hw/Lab3.ipynb) 
* [Lab #4 - Gene Expression]({{ site.baseurl }}/data/hw/GeneExpression.docx) (Due: Tuesday, 02/21/2023 by noon) 
    * [Lab 4 Notebook]({{ site.baseurl }}/data/hw/Lab4.ipynb) 
<hr>
* Lab #5 - Pathogen Identification (Due: Wednesday, 03/08/2023; submit through [Blackboard](http://easternct.blackboard.com))
	* [PDF]({{ site.baseurl }}/data/hw/Lab5_PathogenIdentification.pdf) |
	  [Zip file]({{ site.baseurl }}/data/hw/lab5.zip) 
{% comment %}
* We are skipping Lab 4, and will come back to it if time allows
* [Lab #5 - GenBank]({{ site.baseurl }}/data/hw/Lab5_GenBank.docx) (Due: Monday, 03/07/22) 
* [Lab #6 - Biopython]({{ site.baseurl }}/data/hw/Biopython_MAOA.zip) (Due: Wednesday, 03/23/22; Note that you may not use your grace period for this assignment)
* [Cancer Biology Assignment (Proposed Methods)]({{ site.baseurl }}/data/hw/GroupMethods.pdf) (Due: Monday, 3/28; Note that you may not use your grace period for this assignment) 
* [Lab #7 - Pairwise Alignments]({{ site.baseurl }}/data/hw/PairwiseAlignment.docx) (Due: Wednesday, 04/13/22)
* [Lab #8 - Dynamic Programming]({{ site.baseurl }}/data/hw/DynamicProgramming.docx) (Due: Wednesday, 04/20/22)
</div>
* [Cancer Bio Presentation]({{ site.baseurl }}/data/hw/FinalPresentation.pdf) (Due: Wednesday, 05/04/22 by 5:00 PM; Note that you may not use your grace period for this assignment)
* Group Project Post Survey (Due: Friday, 5/6/22 by 5:00 PM; will be posted on <a href = 'https://easternct.blackboard.com'>Blackboard</a>)
* Final Project ([Assignment]({{ site.baseurl }}/data/hw/FinalProject.pdf) 
   | [Rubric]({{ site.baseurl }}/data/hw/FinalProjectRubric.pdf)) (You may not use your grace period for the final project)
    * Project selection (Blackboard; Due Monday, 05/02/22 by 10:00 AM)
    * Project due date: 10:00 AM on 05/13/22 (submit through Blackboard) 


<br><br>
<center>
<div id = 'clicker'>
<a href = '#' style='font-size:120%' onclick = 'viewAll();'>Click to view all assignments</a>
<script>
function viewAll() {
    document.getElementById('hidden').classList.remove('hide');
    document.getElementById('clicker').classList.add('hide');
    document.getElementsByTagName('ul')[0].style.marginBottom = '0px'
}
</script>


{% endcomment %}

<script>
const pattern = RegExp('Due:.*([0-9]{2}/[0-9]+/[0-9]{4})');
elements = document.getElementsByTagName('li');

for (el of elements) {
        var res = pattern.exec(el.innerText);
        if (res != null && res.length >= 2) {
                if (new Date(res[1]) >= new Date()) {
                        el.className = 'due';
                }
        }
}
</script>
