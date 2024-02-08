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
* Install the required software on your personal computer, by following the Software installation instructions on the [Course Info](../info/) page. We will begin using Python in late January / early February.
<!--<hr style = 'height:1px; background-color:maroon'> -->
* [Lab #1 - OMIM and Inheritance]({{ site.baseurl }}/data/hw/Lab1_OMIM.docx) (Due: Thursday, 02/01/2024) 
* [Lab #2 - Python Lab]({{ site.baseurl }}/data/hw/Lab2.ipynb) (Due: Tuesday, 02/06/2024; submit through [Blackboard](http://easternct.blackboard.com))
* Lab #3 - DNA and complements (Due: Thursday, 02/08/2024, submit through [Blackboard](http://easternct.blackboard.com))
    * [Lab #3 DNA Questions]({{ site.baseurl }}/data/hw/Lab3_Complements.docx)
    * [Lab #3 Notebook]({{ site.baseurl }}/data/hw/Lab3.ipynb) 
<hr>
* [Lab #4 - Gene Expression]({{ site.baseurl }}/data/hw/GeneExpression.docx) (Due: Thursday, 02/15/2024; submit a hard copy at the beginning of class) 
{% comment %}
    * [Lab 4 Notebook]({{ site.baseurl }}/data/hw/Lab4.ipynb) 
* Lab #5 - Pathogen Identification (Due: Wednesday, 03/08/2024; submit through [Blackboard](http://easternct.blackboard.com))
	* [PDF]({{ site.baseurl }}/data/hw/Lab5_PathogenIdentification.pdf) |
	  [Zip file]({{ site.baseurl }}/data/hw/lab5.zip) 
* [Lab #6 - GenBank]({{ site.baseurl }}/data/hw/Lab6_GenBank.docx) (Due: Friday, 03/10/2024; submit hardcopy in class) 
{% comment %}
</div>
{% endcomment %}

* [Lab #7 - Biopython]({{ site.baseurl }}/data/hw/Biopython_MAOA.zip) (Due: Wednesday, 03/22/2024; submit through [Blackboard](http://easternct.blackboard.com))
* [Lab #8 - Pairwise Alignments]({{ site.baseurl }}/data/hw/PairwiseAlignment.docx) (Due: Friday, 03/24/2024)
* [Lab #9 - Dynamic Programming]({{ site.baseurl }}/data/hw/DynamicProgramming.docx) (Due: Wednesday, 03/29/2024; submit hardcopy in class)
* [Lab #10 - BLAST]({{ site.baseurl }}/data/hw/Lab10_BLAST_Covid.docx) (Due: Monday, 04/03/2024; submit hardcopy in class; you cannot use your grace period)
* [Lab #11 - HMM]({{ site.baseurl }}/data/hw/HMM_lab.pdf) (Due: Wednesday, 04/26/2024; submit hardcopy in class)
* Lab #12 - Use Galaxy ([https://usegalaxy.org](https://usegalaxy.org)) to find the number of genes on each chromosome, not including pseudogenes. Submit a link to your history on [Blackboard](https://easternct.blackboard.com). Due: Monday, 05/01/2024 by 1:00 PM (you may not use your grace period on this assignment)  
* Final Project ([Assignment]({{ site.baseurl }}/data/hw/FinalProject.pdf) 
   | [Rubric]({{ site.baseurl }}/data/hw/FinalProjectRubric.pdf)) (You may not use your grace period for the final project)
    * Project selection (Due: Monday, 05/01/2024 by 1:00 PM, answer on [Blackboard](http://easternct.blackboard.com))
    * Final Project (Due: 4:00 PM on 05/08/2024, submit through [Blackboard](http://easternct.blackboard.com)) 
* [Cancer Biology Assignment (Proposed Methods)]({{ site.baseurl }}/data/hw/GroupMethods.pdf) (Due: Monday, 3/28; Note that you may not use your grace period for this assignment) 
</div>
* [Cancer Bio Presentation]({{ site.baseurl }}/data/hw/FinalPresentation.pdf) (Due: Wednesday, 05/04/22 by 5:00 PM; Note that you may not use your grace period for this assignment)
* Group Project Post Survey (Due: Friday, 5/6/22 by 5:00 PM; will be posted on <a href = 'https://easternct.blackboard.com'>Blackboard</a>)


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
