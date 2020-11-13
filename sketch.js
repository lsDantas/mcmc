//Simulation constants
const n_weeks = 10000
var positions = Array(n_weeks).fill(0)
var current = 10
var i = 0
var counts = Array(10).fill(0)
var islands = [{x:181, y:112, r : 1}, 
    {x: 84, y:188, r : 2}, 
    {x : 50, y : 306, r : 3}, 
    {x : 92, y : 423, r : 4}, 
    {x : 194, y : 492, r : 5},
    {x : 318, y : 487, r : 6}, 
    {x : 415, y : 411, r : 7}, 
    {x : 449, y : 293, r :8}, 
    {x : 407, y : 176, r :9}, 
    {x : 305, y : 107, r : 10}]

var lines = Array(5).fill({start : [islands[current-1].x, islands[current-1].y], end : [islands[current-1].x, islands[current-1].y], ind : 1})

function flipCoin(){
    /* Function that flip a coin, if is head, return -1, if is tail, return 1
     */
    var unif = Math.random()
    var coin = unif > 0.5 ? 1 : -1
    return coin
}


var fr = 24 

function setup() {
    createCanvas(800, 600)
    background(0)
    frameRate(fr)
}
  
function draw() {
    if(i < n_weeks){ 
        positions[i] = current
        counts[current -1] = counts[current-1] + 1

        //proposal 
        var proposal = current + flipCoin()
        //Fix if it is outsite [1, 10]
        //If pass 10, go to 1
        proposal = proposal > 10 ? 1 : proposal
        //If pass 1, go to 10
        proposal = proposal < 1 ? 10 : proposal

        //should he move?
        var prob_move = proposal/current
        var unif = Math.random()
        current = unif < prob_move ? proposal : current

        i = i+1;

        background(0)
        strokeWeight(1)
        noFill()
        stroke('white')
        circle(250, 300, 400)

        noStroke()
        textSize(20)
        fill("white")
        text('Tale of King Markov and Mr Metropolis', 50, 50)
        

        //Draw histogram
        var max_count = Math.max(...counts.map(d =>d)) 
        noStroke()
        fill('blue')
        textSize(15)
        text('Fraction of visits in each island', 550, 250)
        counts.forEach( (d, j) => {
            fill('white')          
            rect(550 + j*20, 400, 20, -d*100/max_count)
            noStroke()
            fill('blue')
            rect(551 + j*20, 400, 18, -d*100/max_count+ 2)
            textSize(15)
            textStyle(BOLD)
            text(j + 1, 550 + j*21, 420)
        })

        //Draw islands
        islands.forEach((d) => {
            circle(d.x, d.y, d.r*3 + 20)
        })
        
        //remove oldest line
        lines.shift()
        //add newest line
        lines.push({start : lines[lines.length - 1].end, end : [islands[current-1].x, islands[current-1].y], ind : 1})
        
        //Draw lines
        lines.forEach((d, j) => {
            let r = Math.floor(255 * (j/10))
            let b = 255 * j/(lines.length  - 1)
            stroke('rgba('+r+ ', 0, 0, 1)')
            strokeWeight(j*j)
            line(d.start[0], d.start[1], d.end[0], d.end[1])
        })

        //Draw king
        fill(255, 255, 51)
        noStroke()
        circle(islands[current - 1].x + Math.random()*10, islands[current-1].y+Math.random()*10, 20)

    }
}

