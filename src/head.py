head = """
% !TeX document-id = {a9da8c09-8ca2-42d8-97aa-816e53d9f143}
% !TeX TXS-program:compile = txs:///latexmk/{}[-xelatex -synctex=1 -interaction=nonstopmode -silent %.tex]

\documentclass[hideanswer=true,
enfont=empty,	%在settings.tex里由zhfont指定
zhfont=empty,	%在settings.tex里由zhfont指定
mathfont=newtxmath,
]{cmcthesis}

\cmcthesissetup{% key = value 设置处
	%
}

\input{settings.tex}
\begin{document}

	\cmcthesistitle{
		name    = 嘉善县火种计划试点学校信息技术阶段测试 ,
		subname = Python 试题,
		date    =  2021年6月 \thinspace , % 9:00 - 11:30  ,
%		author  = (火种计划命题组)  ,
		motto   = 技术支持：红码科技,
	}

\addvspace{1\bigskipamount}
"""