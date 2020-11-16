class islandsObj {
    constructor(x, y, r){
        this.x = x
        this.y = y
        this.r = r
        this.islands_coords = Array(10).fill().map(function(d, i){
            return {x : Math.cos(Math.PI/5* i), y: Math.sin(Math.PI / 5 * i), r : i + 1}
        })
    }

    get_position(i){
        return [this.islands_coords[i].x * this.r + this.x,
                this.islands_coords[i].y * this.r + this.y]
    }

    draw(){
        //Bigger circle
        stroke(0)
        strokeWeight(1)
        noFill()
        circle(this.x, this.y, 2*this.r)

        //Islands
        noStroke()
        fill("blue")
        this.islands_coords.forEach(d => {
            circle(d.x * this.r + this.x, d.y * this.r + this.y, 10 + d.r*3)
        })
    }
}

class kingObj{
    constructor(r, init, total_travels, islands){
        this.r = r
        this.pos = islands.get_position(init)
        this.islands = islands
        this.last_arrivals = Array(total_travels).fill(this.pos)
        this.last_departures = Array(total_travels).fill(this.pos)
        this.total_travels = total_travels
    }

    new_travel(index){
        //remove oldest travel
        this.last_arrivals.shift()
        this.last_departures.shift()

        //add new travel
        this.last_departures.push(this.last_arrivals[this.total_travels - 2])
        this.last_arrivals.push(this.islands.get_position(index - 1))
        this.pos = this.last_arrivals[this.total_travels - 1]
    }

    draw(){       
        stroke(255, 0, 0)
        //draw lines
        for(let i = 0; i < this.total_travels; i++){
            strokeWeight(i * i + 2)
            let p0 = this.last_arrivals[i]
            let p1 = this.last_departures[i]
            line(p0[0], p0[1], p1[0], p1[1])
        }
		
		//draw King
        noStroke()
        fill(255, 255, 51)
        circle(this.pos[0] + Math.random() * 5, this.pos[1] + Math.random() * 5, this.r)
        

    }
}

class histObj{
    constructor(x, y){
        this.x = x
        this.y = y
    }

    draw(counts){
        var max_count = Math.max(...counts.map(d =>d)) 
        noStroke()
        fill('black')
        textSize(15)
        textStyle(BOLD)
        text('Fraction of visits in each island', this.x, this.y - 150)
        stroke(0)
        strokeWeight(3)
        line(this.x, this.y+1, this.x + 11*20, this.y+1)
        line(this.x, this.y+1, this.x, this.y - 110)
        counts.forEach( (d, j) => {
            fill('black')          
            rect(this.x + j*20, this.y, 20, -d*100/max_count)
            noStroke()
            fill('blue')
            rect(this.x + 1 + j*20, this.y, 18, -d*100/max_count+ 2)
            fill('black')
            textSize(15)
            textStyle(BOLD)
            text(j + 1, this.x + j*21, this.y + 20)
            textStyle(NORMAL)
            text('Island', this.x + 80, this.y + 40)
        })
    }
}


//Simulation constants
const n_weeks = 10000
var positions = Array(n_weeks).fill(0)
var current = 10
var week = 0
var counts = Array(10).fill(0)


var islands = new islandsObj(250, 300, 200)
var king = new kingObj(20, 9, 5, islands)
var hist = new histObj(550, 250)


function flipCoin(){
    /* Function that flip a coin, if is head, return -1, if is tail, return 1
     */
    var unif = Math.random()
    var coin = unif > 0.5 ? 1 : -1
    return coin
}


var fr = 24 

function setup() {
    createCanvas(800, 550)
    background(255)
    frameRate(fr)
}
  
function draw() {
    if(week < n_weeks){ 
        positions[week] = current
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

        week = week+1;


        //Drawing simulation
        background(255)

        //Title
        noStroke()
        textSize(20)
        fill("black")
        text('Tale of King Markov and Mr Metropolis', 50, 50)
        textSize(15)
        text('Week: '+week, 550, 50)

        //Draw histogram
        hist.draw(counts)

        //Draw islands
        islands.draw()

        //Update king move
        king.new_travel(current)

        //Draw king
        king.draw()

    }
}


