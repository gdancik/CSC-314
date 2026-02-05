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
* [Lab #1 - OMIM and Inheritance]({{ site.baseurl }}/data/hw/Lab1_OMIM.docx) (Due: Thursday, 02/05/2026, submit hard copy at beginning of class) 
* Create a [Google](https://accounts.google.com/) account  if you do not have one
<hr style = 'height:1px; background-color:maroon; margin-top:-6px'> 
* [Lab #2 - Python Lab]({{ site.baseurl }}/data/hw/Lab2.ipynb) (Due: Thursday, 02/12/2026) (turn in a hard copy at the beginning of class)
{% comment %}
* Lab #3 - DNA and complements (Due: Tuesday, 02/18/2025)) (turn in a hard copy)
    * [Lab #3 DNA Questions]({{ site.baseurl }}/data/hw/Lab3_Complements.docx) \| [Lab #3 Notebook]({{ site.baseurl }}/data/hw/Lab3.ipynb) 
* Lab #4 -- Gene Expression and Python dictionaries (Due: Thursday, 02/20/2025) (turn in a hard copy of each)
	* [Lab #4 - Gene Expression]({{ site.baseurl }}/data/hw/GeneExpression.docx) \| [Lab #4 Notebook]({{ site.baseurl }}/data/hw/Lab4.ipynb) 
</div>
* [Lab #5 - GenBank]({{ site.baseurl }}/data/hw/Lab5_GenBank.docx) (Due: Thursday, 03/06/2025; submit hardcopy in class) 
* [Lab #6 - GenPept+]({{ site.baseurl }}/data/hw/ProteinDB.docx) (Due: Tuesday, 03/11/2025; submit through Blackboard) 
* Lab #7 - Pathogen Identification (Due: Tuesday, 03/25/2025; submit through [Blackboard](http://easternct.blackboard.com))
	* [PDF]({{ site.baseurl }}/data/hw/Lab7_PathogenIdentification.pdf) |
	  [Zip file]({{ site.baseurl }}/data/hw/lab7.zip) 
* [Lab #8 - Biopython]({{ site.baseurl }}/data/hw/Biopython_MAOA.zip) (Due: Thursday, 03/27/2025 by 2:00 PM; submit through [Blackboard](http://easternct.blackboard.com))
* [Lab #9 - Pairwise Alignments]({{ site.baseurl }}/data/hw/PairwiseAlignment.docx) (Due: Tuesday, 04/01/2025; submit hardcopy in class)
* [Lab #10 - Dynamic Programming]({{ site.baseurl }}/data/hw/DynamicProgramming.docx) (Due: Thursday, 04/03/2025; submit hardcopy in class; note: for question 3(a) and 3(b), use the optimal <i>semi</i>global alignment; this has been corrected in the assignment)
* [Lab #11 - BLAST]({{ site.baseurl }}/data/hw/Lab11_Blast.pdf) | [sequences.txt]({{ site.baseurl }}/data/hw/sequences.txt) 
(Due: <strike>Tuesday, 04/08/2025</strike> Thursday, 04/10/2025; submit hardcopy in class; you cannot use your grace period)
* Lab #12 - Gene Prediction (Due: Thursday, 04/24/2025; submit through [Blackboard](http://easternct.blackboard.com))
	* [Gene Prediction]({{ site.baseurl }}/data/hw/GenePrediction.docx) |
	  [sequences.fasta]({{ site.baseurl }}/data/hw/sequences.fasta) 
* [Lab #13 - HMM and Galaxy]({{ site.baseurl }}/data/hw/CSC314_Lab13.docx)
(Due: Thursday, 05/01/2025; submit through [Blackboard](https://easternct.blackboard.com)) 
	* [human_genes_partial.tsv]({{ site.baseurl }}/data/notes/human_genes_partial.tsv)
	* [human_genes.tsv]({{ site.baseurl }}/data/notes/human_genes.tsv)
* Final Project ([Assignment]({{ site.baseurl }}/data/hw/FinalProject.pdf) 
   | [Rubric]({{ site.baseurl }}/data/hw/FinalProjectRubric.pdf)) (You may not use your grace period for the final project)
    * Project selection (Due: 5:00 PM on 05/06/2025; answer on [Blackboard](http://easternct.blackboard.com))
    * Final Project (Due: 4:00 PM on 05/13/2025, submit through [Blackboard](http://easternct.blackboard.com)) 
    * [Lab 4 Notebook]({{ site.baseurl }}/data/hw/Lab4.ipynb) 
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
