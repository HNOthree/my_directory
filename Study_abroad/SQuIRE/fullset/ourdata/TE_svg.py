import pandas as pd
import argparse
from cairosvg import svg2png
parser = argparse.ArgumentParser()
parser.add_argument('-e', help='enrichment file')
parser.add_argument('-i', help='input file')
parser.add_argument('-o',help='output directory')
parser.add_argument('-t', help='threshold') 
parser.add_argument('-c', help='chromosome file')
parser.add_argument('-p', help='png file(if you want). You MUST make "png" directory at output directory')
args = parser.parse_args()
chromosome_enrichment_file=args.e
input_file=args.i
out_dir=args.o
bias_thres=float(args.t)
chromosome_file=args.c


def svgwrite(status,start,end,sexuality,chrLen,TE_lfc):
 x_start=50
 window=1000
 if(end>chrLen):
  end=chrLen
 if (status=="enrich"):
  y_axis="135"
  opacity=1
 elif(status=="TE"):
  y_axis="100"
  opacity=abs(TE_lfc)/15 
 if(sexuality=="male"):
  colour="blue"
 elif(sexuality=="female"):
  colour="red"
 else:
  colour="green"
 start_pos=int(start/chrLen*window)+x_start
 length=int((end-start)/chrLen*window)
 if(length==0):
  length=1
 output_line='<rect x ="{}" y="{}" width="{}" height="20" fill="{}" fill-opacity="{}"/>'.format(start_pos,y_axis,length,colour,opacity)
 return output_line


def my_function():
 chrdata=pd.read_csv(chromosome_file,sep='\t',names=("Chr","Length"))
 enrich=pd.read_csv(chromosome_enrichment_file,sep='\t',names=("Chr","Start_region","End_region","Sexuality"))
 TE_genedata=pd.read_csv(input_file,sep='\t')
 male_data=TE_genedata[TE_genedata.Log2FoldChange>bias_thres]
 male_data["Sexuality"]="male"
 female_data=TE_genedata[TE_genedata.Log2FoldChange<-bias_thres]
 female_data["Sexuality"]="female"
 other_data=TE_genedata[abs(TE_genedata.Log2FoldChange)<1]
 other_data["Sexuality"]="neutral"
 biassed_data=male_data.append(female_data)
 biassed_data=biassed_data.append(other_data)
 print("Absolute value of expression is more than",bias_thres)
 print("The number of satisfied data",len(biassed_data))
 x_start=50
 window=1000

 for i in range(0,len(chrdata)):
  chrLen=chrdata.iloc[i].Length
  chrName=chrdata.iloc[i].Chr
  enrich_chr=enrich[enrich.Chr==chrName]
  bias_chr=biassed_data[biassed_data.Chr==chrName]
  output_file=out_dir+"/{}_{}.svg".format(chrName,bias_thres)
  with open(output_file,"w")as f: 
   svg_code=""
   svg_code+='<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="250" viewBox="0 0 1100 250">'
   svg_code+='<path d="M0 0 L 1100 0 L 1100 250 L 0 250" style="fill:#FFFFFF;stroke-width:0" />'
   svg_code+='<text x ="0" y="150" font-style="italic" font-size="40">5`</text>'
   svg_code+='<text x ="30" y="50" font-size="30">{}</text>'.format(chrName)
   svg_code+='<text x ="1050" y="150" font-style="italic" font-size="40">3`</text>'
   svg_code+='<text x ="50" y="100" font-size="20">TE</text>'
   svg_code+='<text x ="50" y="170" font-size="20">Active region</text>'
   svg_code+='<rect x ="{}" y="120" width="{}" height="15"/>'.format(x_start,int(chrLen/chrLen*window))
   f.write('<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="250" viewBox="0 0 1100 250">')
   f.write('<path d="M0 0 L 1100 0 L 1100 250 L 0 250" style="fill:#FFFFFF;stroke-width:0" />')
   f.write('<text x ="0" y="150" font-style="italic" font-size="40">5`</text>')
   f.write('<text x ="30" y="50" font-size="30">{}</text>'.format(chrName))
   f.write('<text x ="1050" y="150" font-style="italic" font-size="40">3`</text>')
   f.write('<text x ="50" y="100" font-size="20">TE</text>')
   f.write('<text x ="50" y="170" font-size="20">Active region</text>')
   f.write('<rect x ="{}" y="120" width="{}" height="15"/>'.format(x_start,int(chrLen/chrLen*window)))
   for j in range(len(enrich_chr)):
    en_info=enrich_chr.iloc[j]
    sentence=svgwrite("enrich",en_info.Start_region,en_info.End_region,en_info.Sexuality,chrLen,0)
    svg_code+=sentence
    f.write(sentence)

   for j in range(len(bias_chr)):
    bias_info=bias_chr.iloc[j]
    sentence=svgwrite("TE",bias_info.Start_TE,bias_info.End_TE,bias_info.Sexuality,chrLen,bias_info.Log2FoldChange)
    svg_code+=sentence
    f.write(sentence)
 
   svg_code+="</svg>"
   if(args.p!=""):
    png_output=out_dir+"/png/output{}_{}.png".format(chrName,bias_thres)
    svg2png(bytestring=svg_code,write_to=png_output) 
   f.write("</svg>")

def main():
 thresholds=["25","100"]
 bias_thres=[1,2,3,4]
 for threshold in thresholds:
  for thre in bias_thres:
   my_function(threshold,thre)

#main()

def sample():
 my_function()

sample()
