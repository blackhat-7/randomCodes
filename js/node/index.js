const express = require("express");
const Joi = require("joi");

const courses = [
  {
    id: 1,
    name: "course 1",
  },
  {
    id: 2,
    name: "course 2",
  },
  {
    id: 3,
    name: "course 3",
  },
];

const app = express();

const validate = (name) => {
  const schema = {
    name: Joi.string().min(3).required(),
  };
  const result = Joi.validate(name, schema);
  return result;
};

app.get("/", (_, res) => {
  res.send("Hello World!");
});

app.get("/api/courses", (_, res) => {
  res.send(courses);
});

app.get("/api/courses/:id", (req, res) => {
  const course = courses.find((c) => c.id === parseInt(req.params.id));
  if (!course) {
    res.status(404).send("Course not found!");
  }
  res.send(course);
});

app.post("/api/courses", (req, res) => {
  const { error } = validate(res);

  if (error) {
    res.status(400).send(error.details[0].message);
  }
  const course = {
    id: course.length + 1,
    name: req.body.name,
  };
  courses.push(course);
  res.send(course);
});

app.put("/api/courses", (res, _) => {
  const course = courses.find((c) => c.id === parseInt(res.params.id));
  if (!course) {
    res.status(404).send(`No course with id ${res.params.id}`);
    return;
  }

  const { error } = validate(res);

  if (error) {
    res.status(400).send(error.details[0].message);
  }

  course.name = res.body.name;
  res.send(course);
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening at port ${port}`));
