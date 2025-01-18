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

<div id = 'hidden' class = 'shide' markdown="1">
* Watch the You Tube videos covering Genes, SNPs, and Where Your Genes Come From linked in the <a href = "../notes/">Course Introduction</a> notes
<!--<hr style = 'height:1px; background-color:maroon'> -->
{% comment %}
* [Lab #1 - OMIM and Inheritance]({{ site.baseurl }}/data/hw/Lab1_OMIM.docx) (Due: Thursday, 02/01/2024) 
* [Lab #2 - Python Lab]({{ site.baseurl }}/data/hw/Lab2.ipynb) (Due: Tuesday, 02/06/2024; submit through [Blackboard](http://easternct.blackboard.com))
* Lab #3 - DNA and complements (Due: Thursday, 02/08/2024, submit through [Blackboard](http://easternct.blackboard.com))
    * [Lab #3 DNA Questions]({{ site.baseurl }}/data/hw/Lab3_Complements.docx)
    * [Lab #3 Notebook]({{ site.baseurl }}/data/hw/Lab3.ipynb) 
* [Lab #4 - Gene Expression]({{ site.baseurl }}/data/hw/GeneExpression.docx) (Due: Thursday, 02/15/2024; submit a hard copy at the beginning of class) 
</div>
* [Lab #5 - GenBank]({{ site.baseurl }}/data/hw/Lab5_GenBank.docx) (Due: Tuesday, 03/05/2024; submit hardcopy in class) 
* [Lab #6 - GenPept+]({{ site.baseurl }}/data/hw/ProteinDB.docx) (Due: Thursday, 03/07/2024; submit through Blackboard) 
* [Lab #7 - Biopython]({{ site.baseurl }}/data/hw/Biopython_MAOA.zip) (Due: Friday, 03/08/2024 by 2:00 PM; submit through [Blackboard](http://easternct.blackboard.com))
* [Lab #8 - Pairwise Alignments]({{ site.baseurl }}/data/hw/PairwiseAlignment.docx) (Due: Tuesday, 03/26/2024; submit hardcopy in class)
* [Lab #9 - Dynamic Programming]({{ site.baseurl }}/data/hw/DynamicProgramming.docx) (Due: Tuesday, 04/02/2024; submit hardcopy in class)
* [Lab #10 - BLAST]({{ site.baseurl }}/data/hw/Lab10_Blast.pdf) | [sequences.txt]({{ site.baseurl }}/data/hw/sequences.txt) 
(Due: Thursday, 04/04/2024; submit hardcopy in class; you cannot use your grace period)
* [Lab #11 - HMM]({{ site.baseurl }}/data/hw/HMM_lab.pdf) (Due: Tuesday, 04/23/2024; submit hardcopy in class)
* Lab #12 - Use Galaxy ([https://usegalaxy.org](https://usegalaxy.org)) to find the number of genes on each chromosome, not including pseudogenes. Submit a link to your history for both the partial and complete gene lists on [Blackboard](https://easternct.blackboard.com) (Due: Thursday, 04/25/2024)  
<hr>
* Final Project ([Assignment]({{ site.baseurl }}/data/hw/FinalProject.pdf) 
   | [Rubric]({{ site.baseurl }}/data/hw/FinalProjectRubric.pdf)) (You may not use your grace period for the final project)
    * Project selection (Due: Tuesday, 04/30/2024 by 5:00 PM, answer on [Blackboard](http://easternct.blackboard.com))
    * Final Project (Due: 4:00 PM on 05/09/2024, submit through [Blackboard](http://easternct.blackboard.com)) 

    * [Lab 4 Notebook]({{ site.baseurl }}/data/hw/Lab4.ipynb) 
* Lab #5 - Pathogen Identification (Due: Wednesday, 03/08/2024; submit through [Blackboard](http://easternct.blackboard.com))
	* [PDF]({{ site.baseurl }}/data/hw/Lab5_PathogenIdentification.pdf) |
	  [Zip file]({{ site.baseurl }}/data/hw/lab5.zip) 

* [Cancer Biology Assignment (Proposed Methods)]({{ site.baseurl }}/data/hw/GroupMethods.pdf) (Due: Monday, 3/28; Note that you may not use your grace period for this assignment) 
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
