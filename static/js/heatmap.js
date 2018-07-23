  var cam2num = {'ACC': 1,
 'BLCA': 2,
 'BRCA': 3,
 'CESC': 4,
 'CHOL': 5,
 'COAD': 6,
 'DLBC': 7,
 'ESCA': 8,
 'GBM': 9,
 'HNSC': 10,
 'KICH': 11,
 'KIRC': 12,
 'KIRP': 13,
 'LAML': 14,
 'LGG': 15,
 'LIHC': 16,
 'LUAD': 17,
 'LUSC': 18,
 'MESO': 19,
 'OV': 20,
 'PAAD': 21,
 'PCPG': 22,
 'PRAD': 23,
 'READ': 24,
 'SARC': 25,
 'SKCM': 26,
 'STAD': 27,
 'TGCT': 28,
 'THCA': 29,
 'THYM': 30,
 'UCEC': 31,
 'UCS': 32,
 'UVM': 33}
;
  var margin = { top: 20, right: 0, bottom: 50, left: 50 },
      buckets = 9,
      colors = colorbrewer.GnBu[9]
      days = ["Tumor", "Normal"],
      times = ['ACC', 'BLCA', 'BRCA', 'CESC', 'CHOL', 'COAD', 'DLBC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP','LAML', 'LGG', 'LIHC', 'LUAD', 'LUSC', 'MESO', 'OV', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'SKCM', 'STAD', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UCS', 'UVM'];

  var heatmapChart = function(data, target, inwidth, inheight) {
      var width = inwidth - margin.left - margin.right, // 960 * 170
      gridSize = Math.floor(width / 33),
      height = inheight - margin.top - gridSize,
      legendElementWidth = gridSize*2

      var svg = d3.select('#' + target).append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      var dayLabels = svg.selectAll(".dayLabel")
          .data(days)
          .enter().append("text")
            .text(function (d) { return d; })
            .attr("x", 0)
            .attr("y", function (d, i) { return i * gridSize; })
            .style("text-anchor", "end")
            .attr("transform", "translate(-6," + gridSize / 1.5 + ")")
            //.attr("class", function (d, i) { return ((i >= 0 && i <= 4) ? "dayLabel mono axis axis-workweek" : "dayLabel mono axis"); });
            .attr("class", "dayLabel mono axis");


      var timeLabels = svg.selectAll(".timeLabel")
          .data(times)
          .enter().append("text")
            .text(function(d) { return d; })
            .attr("x", function(d, i) { return i * gridSize; })
            .attr("y", 0)
            .style("text-anchor", "middle")
            .attr("transform", "translate(" + gridSize / 2 + ", -6)")
            //.attr("class", function(d, i) { return ((i >= 7 && i <= 16) ? "timeLabel mono axis axis-worktime" : "timeLabel mono axis"); });
            .attr("class", "timeLabel mono axis");

      var colorScale = d3.scale.quantile()
          //.domain([0, buckets - 1, d3.max(data, function (d) { return d.value; })])
          .domain([0, d3.max(data, function (d) { return d.value; })])
          .range(colors);

      var cards = svg.selectAll(".hour")
          .data(data, function(d) {return d.day+':'+d.hour;});

      cards.append("title");

      cards.enter().append("rect")
          .attr("x", function(d) { return (d.hour - 1) * gridSize; })
          .attr("y", function(d) { return (d.day - 1) * gridSize; })
          .attr("rx", 4)
          .attr("ry", 4)
          .attr("class", "hour bordered")
          .attr("width", gridSize)
          .attr("height", gridSize)
          .style("fill", colors[0]);

      cards.transition().duration(1000)
          .style("fill", function(d) { return colorScale(d.value); });

      cards.select("title").text(function(d) { return d.value; });
      
      cards.exit().remove();

      var legend = svg.selectAll(".legend")
          .data([0].concat(colorScale.quantiles()), function(d) { return d; });

      legend.enter().append("g")
          .attr("class", "legend");

      legend.append("rect")
        .attr("x", function(d, i) { return legendElementWidth * i + width / 4; })
        .attr("y", height)
        .attr("width", legendElementWidth)
        .attr("height", gridSize / 2)
        .style("fill", function(d, i) { return colors[i]; });

      legend.append("text")
        .attr("class", "mono")
        .text(function(d) { return "≥ " + Math.round(d); })
        .attr("x", function(d, i) { return legendElementWidth * i + width / 4; })
        .attr("y", height + gridSize);

      legend.exit().remove(); 
  };