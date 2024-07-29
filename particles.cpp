#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
// #include <ranges>

#include <fmt/core.h>

struct Particle
{
  float mass;
  std::string name;
  std::string type;
};

bool isBoson(Particle const& p) {
    if (p.type == "boson") {
        return true;
    } else {
        return false;
    }
}

int main()
{
  auto particles = std::vector<Particle> {
    Particle{938.f, "proton", "fermion"},
    Particle{0.f, "photon", "boson"},
    Particle{939.f, "neutron", "fermion"},
    Particle{0.5f, "electron", "fermion"},
    Particle{125000.f, "higgs", "boson"}
    /* may other particles */
  };

  // 1) Find lightest particle

  // 2) Put all bosons to the beginning of the vector
  auto begin = particles.begin();
  auto end = particles.end();
  auto it = std::partition(
   begin,
   end,
   [](Particle const& p){
        return isBoson( p );
    }
  );
  std::cout<< "Il primo fermione e' a distanza: " << std::distance(begin, it) << '\n';

  // auto it_2 = std::ranges::partition(
  //   particles,
  //   isBoson
  // );
}