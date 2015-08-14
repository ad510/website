(ns gen (:require clojure.edn
                  [me.raynes.fs :as fs])
        (:use net.cgrand.enlive-html)
        (:gen-class))

(deftemplate base "base.htm" [pg]
  [:title] (content ((pg 1) :title))
  [[:a (attr= :href (str (pg 0) ".htm"))]] (add-class "sel")
  [[:.submenu (but (id= ((pg 1) :submenu)))]] nil
  [:#pgcontent] (html-content (slurp (str "src/in/" (pg 0) ".htm"))))

(defn -main []
  (fs/delete-dir "src/out")
  (fs/copy-dir "src/in" "src/out")
  (spit "src/out/emai1.txt" (clojure.string/join (interpose "," (reverse
    (map-indexed (fn [i c] (mod (- (int c) (* i 42) 1) 256)) (slurp "src/emai1.txt"))))))
  (doseq [pg (clojure.edn/read-string (slurp "src/pgs.txt"))]
    (spit (str "src/out/" (pg 0) ".htm") (apply str (base pg)))))
