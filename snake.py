const block_size = 20;

const map = addLevel([
    "==============",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "=            = ",
    "==============",
  ], {
  width: block_size,
  height: block_size,
  pos: vec2(0, 0),
  "=": [
    rect(block_size, block_size),
    color(255,0,0),
    "wall"
  ]
});


const directions = {
  UP: "up",
  DOWN: "down",
  LEFT: "left",
  RIGHT: "right"
};

let current_direction = directions.RIGHT;
let run_loop = false;
let snake_length = 3;
let snake_body = [];


function respawn_snake(){
  destroyAll("snake");

  snake_body = [];
  snake_length = 3;

  for (let i = 1; i <= snake_length; i++) {
      let segment = add([
          rect(block_size ,block_size),
          pos(block_size ,block_size *i),
          color(0,0,255),
          "snake"
      ]);
      snake_body.push(segment);
  };
  current_direction = directions.RIGHT;
}

function respawn_all(){
  run_loop = false;
    wait(0.5, function(){
        respawn_snake();
        run_loop = true;
    });

}

respawn_all();


keyPress("up", () => {
    if (current_direction != directions.DOWN){
        current_direction = directions.UP;
    }
});

keyPress("down", () => {
    if (current_direction != directions.UP){
        current_direction = directions.DOWN;
    }
});

keyPress("left", () => {
    if (current_direction != directions.RIGHT){
        current_direction = directions.LEFT;
    }
});

keyPress("right", () => {
    if (current_direction != directions.LEFT){
        current_direction = directions.RIGHT;
    }
});


loop(0.2, ()=> {
    if (!run_loop) return;

    let move_x = 0;
    let move_y = 0;

    switch (current_direction) {
        case directions.DOWN:
            move_x = 0;
            move_y = block_size;
            break;
        case directions.UP:
            move_x = 0;
            move_y = -1*block_size;
            break;
        case directions.LEFT:
            move_x = -1*block_size;
            move_y = 0;
            break;
        case directions.RIGHT:
            move_x = block_size;
            move_y = 0;
            break;
    }

    // Get the last element (the snake head)
    let snake_head = snake_body[snake_body.length - 1];

    snake_body.push(add([
        rect(block_size,block_size),
        pos(snake_head.pos.x + move_x, snake_head.pos.y + move_y),
        color(0,0,255),
        "snake"
    ]));

    if (snake_body.length > snake_length){
        let tail = snake_body.shift(); // Remove the last of the tail
        destroy(tail);
    }

});


let food = null;

function respawn_food(){
    let new_pos = rand(vec2(1,1), vec2(13,13));
    new_pos.x = Math.floor(new_pos.x);
    new_pos.y = Math.floor(new_pos.y);
    new_pos = new_pos.scale(block_size);

    if (food){
        destroy(food);
    }
    food = add([
                rect(block_size ,block_size),
                color(0,255,0),
                pos(new_pos),
                "food"
            ]);
}

function respawn_all(){
  run_loop = false;
    wait(0.5, function(){
        respawn_snake();
        respawn_food();
        run_loop = true;
    });
}

overlaps("snake", "food", (s, f) => {
    snake_length ++;
    respawn_food();
});

overlaps("snake", "wall", (s, w) => {
    run_loop = false;
    camShake(12);
    respawn_all();
});


overlaps("snake", "snake", (s, t) => {
    run_loop = false;
    camShake(12);
    respawn_all();
});

function respawn_food(){
    let new_pos = rand(vec2(1,1), vec2(13,13));
    new_pos.x = Math.floor(new_pos.x);
    new_pos.y = Math.floor(new_pos.y);
    new_pos = new_pos.scale(block_size);

    if (food){
        destroy(food);
    }
    food = add([
                sprite('pizza'),
                pos(new_pos),
                "food"
            ]);
}

layers([
    "background",
    "game"
], "game");

add([
    sprite("background"),
    layer("background")
])

const map = addLevel([
    "1tttttttttttt2",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "l            r ",
    "3bbbbbbbbbbbb4",
  ], {
    width: block_size,
    height: block_size,
    pos: vec2(0, 0),
    "t": [
      sprite("fence-top"),
      "wall"
    ],
    "b": [
      sprite("fence-bottom"),
      "wall"
    ],
    "l": [
      sprite("fence-left"),
      "wall"
    ],
    "r": [
      sprite("fence-right"),
      "wall"
    ],
    "1": [
      sprite("post-top-left"),
      "wall"
    ],
    "2": [
      sprite("post-top-right"),
      "wall"
    ],
    "3": [
      sprite("post-bottom-left"),
      "wall"
    ],
    "4": [
      sprite("post-bottom-right"),
      "wall"
    ],
  });

function respawn_snake(){
  snake_body.forEach(segment => {
      destroy(segment);
    });
  snake_body = [];
  snake_length = 3;

  for (let i = 1; i <= snake_length; i++) {
      snake_body.push(add([
          sprite('snake-skin'),
          pos(block_size  ,block_size * i),
          "snake"
      ]));
  }
  current_direction = directions.RIGHT;
}

snake_body.push(add([
    sprite('snake-skin'),
    pos(snake_head.pos.x + move_x, snake_head.pos.y + move_y),
    "snake"
]));
